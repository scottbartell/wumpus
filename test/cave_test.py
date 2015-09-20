from lib.wumpus.cave import Cave
from lib.wumpus.room import Room
import unittest


class TestCave(unittest.TestCase):

    def test_it_connects_rooms_properly(self):
        """it has rooms that connect to exactly three other rooms"""
        cave = Cave.dodecahedron()
        rooms = []
        for i in range(20):
            rooms.append(cave.room(i + 1))

        for room in rooms:
            self.assertEqual(len(room.neighbors), 3)
            for neighbor in room.neighbors:
                self.assertTrue(room in neighbor.neighbors)

    def test_it_can_select_rooms_at_random(self):
        """it can select rooms at random"""
        cave = Cave.dodecahedron()
        rooms = []
        for i in range(20):
            rooms.append(cave.room(i + 1))

        self.assertTrue([cave.random_room in rooms])

    def test_it_can_move_hazards_from_one_room_to_another(self):
        """can move hazards from one room to another"""
        cave = Cave.dodecahedron()
        rooms = []
        for i in range(20):
            rooms.append(cave.room(i + 1))

        room = cave.random_room()
        neighbor = room.neighbors[0]

        room.add("bats")
        self.assertTrue(room.has("bats"))
        self.assertFalse(neighbor.has("bats"))

        cave.move("bats", frm=room, to=neighbor)

        self.assertFalse(room.has("bats"))
        self.assertTrue(neighbor.has("bats"))

    def test_it_can_add_hazards_at_random_to_a_specific_number_of_rooms(self):
        """can add hazards at random to a specific number of rooms"""
        cave = Cave.dodecahedron()
        rooms = []
        for i in range(20):
            rooms.append(cave.room(i + 1))

        cave.add_hazard("bats", 3)
        rooms_with_bats = [room for room in rooms if room.has("bats")]
        self.assertEqual(len(rooms_with_bats), 3)

    def test_it_find_a_room_with_a_particular_hazard(self):
        """can find a room with a particular hazard"""
        cave = Cave.dodecahedron()
        rooms = []
        for i in range(20):
            rooms.append(cave.room(i + 1))

        cave.add_hazard("wumpus", 1)
        self.assertTrue(cave.room_with("wumpus").has("wumpus"))

    def test_it_can_find_a_safe_room_for_an_entrance(self):
        """can find a safe room to serve as an entrance"""
        cave = Cave.dodecahedron()
        rooms = []
        for i in range(20):
            rooms.append(cave.room(i + 1))

        cave.add_hazard("wumpus", 1)
        cave.add_hazard("pit", 3)
        cave.add_hazard("bats", 3)

        entrance = cave.entrance()
        self.assertTrue(isinstance(entrance, Room))
        self.assertTrue(entrance.is_safe)
