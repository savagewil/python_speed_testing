from Testees.TestExample import TestExample
from collections import deque


class TestMapAny(TestExample):
    def run(self):

        any(map(self.subfunction, self.data))
