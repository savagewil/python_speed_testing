from Testees.TestExample import TestExample


class TestForLoopListPrebuilt(TestExample):
    def run(self):

        LIST = [0] * len(self.data)
        for i in range(len(self.data)):
            LIST[i] = self.subfunction(self.data[i])
