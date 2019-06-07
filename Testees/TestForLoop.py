from Testees.TestExample import TestExample


class TestForLoop(TestExample):
    def run(self):
        for d in self.data:
            self.subfunction(d)
