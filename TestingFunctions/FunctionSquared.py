from TestingFunctions.FunctionExample import FunctionExample


class FunctionSquared(FunctionExample):
    def run(self, data):
        return data * data

    def run_no_return(self, data):
        data * data
