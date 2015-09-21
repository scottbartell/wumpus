from lib.wumpus.narrator import Narrator
import unittest
from unittest.mock import patch
from io import StringIO


class TestNarrator(unittest.TestCase):

    def test_it_can_ask_for_input(self):
        """it can ask for input"""
        narrator = Narrator()

        with patch("sys.stdin", StringIO("m")), patch('sys.stdout', new=StringIO()) as fakeOutput:
            ask = narrator.ask("What do you want to do? (m)ove or (s)hoot?")
            self.assertEqual(fakeOutput.getvalue(), "What do you want to do? (m)ove or (s)hoot?\n")
            self.assertEqual(ask, "m")

    def test_it_can_say_things(self):
        """it can say things"""
        narrator = Narrator()
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            narrator.say("Well hello there, stranger!")
            self.assertEqual(fakeOutput.getvalue(), "Well hello there, stranger!\n")

    def test_it_knows_when_the_story_is_over(self):
        """it knows when the story is over"""
        narrator = Narrator()
        self.assertFalse(narrator.is_finished)
        narrator.finish_story("It's done!")

        self.assertTrue(narrator.is_finished)

        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            narrator.describe_ending()
            self.assertEqual(fakeOutput.getvalue(), "It's done!\n")

    def test_it_knows_how_to_tell_a_story(self):
        """it knows how to tell a story from beginning to end"""
        narrator = Narrator()
        chapters = [1, 2, 3, 4, 5]

        def function():
            narrator.say("Thus begins chapter " + str(chapters.pop(0)))
            if len(chapters) == 0:
                narrator.finish_story("And they all lived happily ever after!")

        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            narrator.tell_story(function)
            out = fakeOutput.getvalue()
            expected = """Thus begins chapter 1
Thus begins chapter 2
Thus begins chapter 3
Thus begins chapter 4
Thus begins chapter 5
-----------------------------------------
And they all lived happily ever after!
"""
            self.assertEqual(out, expected)

