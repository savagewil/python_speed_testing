from Testees.TestExample import TestExample


class TestForLoopListAppend(TestExample):
    def run(self):
        LIST = [0] * len(self.data)
        for i in range(len(self.data)):
            LIST[i] = self.subfunction(self.data[i])
