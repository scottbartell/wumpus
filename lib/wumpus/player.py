class Player:
    def __init__(self):
        self.senses = {}
        self.encounters = {}
        self.actions = {}
        self.room = None

    def sense(self, thing, callback):
        self.senses[thing] = callback

    def encounter(self, thing, callback):
        self.encounters[thing] = callback

    def action(self, act, callback):
        self.actions[act] = callback

    def enter(self, room):
        self.room = room
        for thing, action in self.encounters.items():
            if room.has(thing):
                return action()

    def act(self, action, room):
        self.actions[action](room)

    def explore_room(self):
        for thing, action in self.senses.items():
            if any([neighbor.has(thing) for neighbor in self.room.neighbors]):
                action()
