import random

class Participant:

    def __init__(self, name):
        self.name = name

    def prepare(self):
        print(f"{self.name}: PREPARE")
        return random.choice([True, True, False])

    def commit(self):
        print(f"{self.name}: COMMIT")

    def rollback(self):
        print(f"{self.name}: ROLLBACK")
