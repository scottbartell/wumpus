from lib.wumpus.room import Room
import json
import os
import random


class Cave:
    @classmethod
    def dodecahedron(cls):
        cave = cls()
        path = os.path.dirname(os.path.realpath(__file__))
        with open(path + '/dodecahedron.json', 'r') as f:
            for (room_num_1, room_num_2) in json.load(f):
                cave.room(room_num_1).connect(cave.room(room_num_2))
        return cave

    def __init__(self):
        self.neighbors = {}

    def room(self, room_number):
        room = self.neighbors.get(room_number, Room(room_number))
        self.neighbors[room_number] = room
        return room

    def random_room(self):
        return random.choice(self.neighbors.values())

    def add_hazard(self, hazard, number_of_rooms):
        rooms = random.sample(self.neighbors.values(), number_of_rooms)
        for room in rooms:
            room.add(hazard)

    def entrance(self):
        for room in self.neighbors.values():
            if room.is_safe():
                return room

    def room_with(self, hazard):
        for room in self.neighbors.values():
            if room.has(hazard):
                return room

    @staticmethod
    def move(hazard, frm, to):
        frm.remove(hazard)
        to.add(hazard)
