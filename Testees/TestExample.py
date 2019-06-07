import time

class TestExample:
    def __init__(self):
        self.subfunction = int
        self.subfunction_class = None
        self.data = []
        self.average_time = 0
        self.current_time = 0

    def setup(self, subfunction, data, return_out=False):
        if subfunction is not None:
            self.subfunction_class = subfunction
            self.subfunction_class.setup()
            if return_out:
                self.subfunction = self.subfunction_class.run
            else:
                self.subfunction = self.subfunction_class.run_no_return
        self.data = data
        self.average_time = 0
        self.current_time = 0

    def __str__(self):
        return str(self.__class__.__name__)

    def run(self):
        pass

    def reset(self):
        self.subfunction_class.reset()

    def start_time(self):
        self.current_time = time.time()

    def end_time(self):
        self.average_time += time.time() - self.current_time


    def __eq__(self, other):
        return self.time == other.time

    def __lt__(self, other):
        return self.time < other.time

    def __gt__(self, other):
        return self.time > other.time

    def __ge__(self, other):
        return self.time >= other.time

    def __le__(self, other):
        return self.time <= other.time

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.time + other.time
        else:
            return self.time + other

    def __radd__(self, other):
        if isinstance(other, self.__class__):
            return self.time + other.time
        else:
            return self.time + other