from Testees.TestExample import TestExample


class TestMapList(TestExample):
    def run(self):
        any(self.subfunction(data) for data in self.data)
