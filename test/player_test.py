from lib.wumpus.player import Player
from lib.wumpus.room import Room
import unittest


class TestPlayer(unittest.TestCase):

    def test_it_can_sense_nearby_hazards(self):
        """can sense nearby hazards"""
        player = Player()
        empty_room = Room(1)
        wumpus_room = Room(2)
        wumpus_room.add("wumpus")
        bat_room = Room(3)
        bat_room.add("bats")
        sensed = set()
        encountered = set()

        empty_room.connect(bat_room)
        empty_room.connect(wumpus_room)

        player.sense("bats", lambda: sensed.add("You hear a rustling"))
        player.sense("wumpus", lambda: sensed.add("You smell something terrible"))
        player.encounter("wumpus", lambda: encountered.add("The wumpus ate you up!"))
        player.encounter("bats", lambda: encountered.add("The bats whisk you away!"))

        player.action("move", lambda destination: player.enter(destination))

        player.enter(empty_room)
        player.explore_room()

        self.assertEqual(sensed, set(["You hear a rustling", "You smell something terrible"]))
        self.assertTrue(len(encountered) == 0)

    def test_it_can_encounter_hazards_when_entering_a_room(self):
        """can encounter hazards when entering a room"""
        player = Player()
        empty_room = Room(1)
        wumpus_room = Room(2)
        wumpus_room.add("wumpus")
        bat_room = Room(3)
        bat_room.add("bats")
        sensed = set()
        encountered = set()

        empty_room.connect(bat_room)
        empty_room.connect(wumpus_room)

        player.sense("bats", lambda: sensed.add("You hear a rustling"))
        player.sense("wumpus", lambda: sensed.add("You smell something terrible"))
        player.encounter("wumpus", lambda: encountered.add("The wumpus ate you up!"))
        player.encounter("bats", lambda: encountered.add("The bats whisk you away!"))

        player.action("move", lambda destination: player.enter(destination))
        player.enter(wumpus_room)
        encountered.clear()
        player.enter(bat_room)
        self.assertEqual(encountered, set(["The bats whisk you away!"]))
        self.assertTrue(len(sensed) == 0)

    def test_it_can_perform_actions(self):
        """can perform actions"""
        player = Player()
        empty_room = Room(1)
        wumpus_room = Room(2)
        wumpus_room.add("wumpus")
        bat_room = Room(3)
        bat_room.add("bats")
        sensed = set()
        encountered = set()

        empty_room.connect(bat_room)
        empty_room.connect(wumpus_room)

        player.sense("bats", lambda: sensed.add("You hear a rustling"))
        player.sense("wumpus", lambda: sensed.add("You smell something terrible"))
        player.encounter("wumpus", lambda: encountered.add("The wumpus ate you up!"))
        player.encounter("bats", lambda: encountered.add("The bats whisk you away!"))

        player.action("move", lambda destination: player.enter(destination))

        player.enter(empty_room)

        self.assertEqual(player.room, empty_room)

        player.act("move", wumpus_room)
        self.assertEqual(player.room, wumpus_room)

        self.assertEqual(encountered, set(["The wumpus ate you up!"]))
        self.assertTrue(len(sensed) == 0)
