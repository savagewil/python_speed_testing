from Testees.TestExample import TestExample


class TestMapList(TestExample):
    def run(self):

        list(map(self.subfunction, self.data))
