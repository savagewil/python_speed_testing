from Testees.TestExample import TestExample
from collections import deque


class TestMapDeque(TestExample):
    def run(self):

        deque(map(self.subfunction, self.data))
