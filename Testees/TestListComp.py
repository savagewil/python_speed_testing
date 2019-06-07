from Testees.TestExample import TestExample


class TestMapList(TestExample):
    def run(self):
        [self.subfunction(data) for data in self.data]
