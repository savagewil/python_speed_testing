from TestingFunctions.FunctionExample import FunctionExample

"""
Warning This Function is very slow, excluding it from the data,
because the individual time segments are long,
making data collection longer and less accurate.
"""
class FunctionExponent(FunctionExample):
    def run(self, data):
        return data ** data

    def run_no_return(self, data):
        data ** data