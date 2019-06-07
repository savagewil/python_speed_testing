from Testees.TestExample import TestExample


class TestForLoopListAppend(TestExample):
    def run(self):

        LIST = []
        for d in self.data:
            LIST.append(self.subfunction(d))
