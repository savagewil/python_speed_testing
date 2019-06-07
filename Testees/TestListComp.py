from Testees.TestExample import TestExample


class TestListComp(TestExample):
    def run(self):

        [self.subfunction(data) for data in self.data]
