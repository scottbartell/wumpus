import random


class Room:
    def __init__(self, number):
        self.number = number
        self.neighbors = []
        self.hazards = []

    def add(self, other):
        self.hazards.append(other)

    def remove(self, other):
        self.hazards.remove(other)

    def has(self, other):
        return other in self.hazards

    def is_empty(self):
        return len(self.hazards) == 0

    def is_safe(self):
        return self.is_empty() and self.neighbors_are_safe()

    def neighbors_are_safe(self):
        return all([neighbor.is_empty() for neighbor in self.neighbors])

    def exits(self):
        return self.neighbors

    def random_neighbor(self):
        if len(self.exits()) == 0:
            return None
        return random.choice(self.exits())

    def connect(self, other_room):
        self.neighbors.append(other_room)
        other_room.neighbors.append(self)
