import sys


class Narrator:
    def __init__(self):
        self.is_finished = False
        self.ending_message = ""

    @staticmethod
    def ask(question):
        sys.stdout.write(question + "\n")
        return sys.stdin.read().strip()

    @staticmethod
    def say(message):
        sys.stdout.write(message + "\n")

    def finish_story(self, message):
        self.is_finished = True
        self.ending_message = message

    def describe_ending(self):
        Narrator.say(self.ending_message)

    def tell_story(self, fcn):
        while not self.is_finished:
            fcn()

        Narrator.say("-----------------------------------------")
        self.describe_ending()
