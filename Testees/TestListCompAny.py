from Testees.TestExample import TestExample


class TestListCompAny(TestExample):
    def run(self):

        any(self.subfunction(data) for data in self.data)
