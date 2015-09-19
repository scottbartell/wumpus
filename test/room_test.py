from lib.wumpus.room import Room
import unittest


class TestRoom(unittest.TestCase):

    def test_it_has_number(self):
        room = Room(12)
        self.assertEqual(room.number, 12)

    def test_it_contains_hazards(self):
        room = Room(12)
        # rooms start out empty
        self.assertTrue(room.is_empty())

        # hazards can be added
        room.add("wumpus")
        room.add("bats")

        # a room with hazards isn't empty
        self.assertFalse(room.is_empty())

        # hazards can be detected by name
        self.assertTrue(room.has("wumpus"))
        self.assertTrue(room.has("bats"))

        self.assertFalse(room.has("alf"))

        # hazards can be removed
        room.remove("bats")
        self.assertFalse(room.has("bats"))

    def test_it_has_two_way_connections_to_neighbors(self):
        room = Room(12)
        exit_numbers = [11, 3, 7]
        for exit_number in exit_numbers:
            room.connect(Room(exit_number))

        for exit_number in exit_numbers:
            # a neighbor can be looked up by room number
            self.assertEqual(room.neighbor(exit_number).number, exit_number)

            # room connections are bidirectional
            self.assertEqual(room.neighbor(exit_number).neighbor(room.number), room)

    def test_it_knows_numbers_of_all_neighbors(self):
        room = Room(12)
        exit_numbers = [11, 3, 7]
        for exit_number in exit_numbers:
            room.connect(Room(exit_number))

        self.assertEqual(room.exits(), exit_numbers)

    def test_it_can_choose_random_neighbor(self):
        room = Room(12)
        exit_numbers = [11, 3, 7]
        for exit_number in exit_numbers:
            room.connect(Room(exit_number))

        self.assertTrue(room.random_neighbor().number in exit_numbers)

    def test_it_is_not_safe_if_it_has_hazards(self):
        room = Room(12)
        exit_numbers = [11, 3, 7]
        for exit_number in exit_numbers:
            room.connect(Room(exit_number))

        room.add("wumpus")
        self.assertFalse(room.is_safe())

    def test_it_is_not_safe_if_neighbors_have_hazards(self):
        room = Room(12)
        exit_numbers = [11, 3, 7]
        for exit_number in exit_numbers:
            room.connect(Room(exit_number))

        room.random_neighbor().add("wumpus")
        self.assertFalse(room.is_safe())

    def test_it_is_safe_when_it_and_its_neighbors_have_no_hazards(self):
        room = Room(12)
        exit_numbers = [11, 3, 7]
        for exit_number in exit_numbers:
            room.connect(Room(exit_number))

        self.assertTrue(room.is_safe())
