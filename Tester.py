import time
from pathlib import Path

from Testees import TestForLoop, TestForLoopListAppend, TestForLoopListPrebuilt
from Testees import TestListComp, TestListCompAny, TestMapAny, TestMapDeque, TestMapList

from TestingFunctions import FunctionExponent, FunctionLargeMath, FunctionPygameCircle


DATA_SIZE = 4000
REPETITIONS = 100
data_file_index = 0
data_file = "./Results/result_%d_%d_%d.md" % (DATA_SIZE, REPETITIONS, data_file_index)
while Path('/path/to/file').is_file():
    data_file_index += 1
    data_file = "./Results/result_%d_%d_%d.md" % (DATA_SIZE, REPETITIONS, data_file_index)
OUT_FILE = open(data_file, 'w')
def print_write(string=""):
    print(string)
    OUT_FILE.write(string + "\n")
DATA = list(range(DATA_SIZE))

TESTEES = [TestForLoop.TestForLoop(), TestForLoopListAppend.TestForLoopListAppend(),
           TestForLoopListPrebuilt.TestForLoopListPrebuilt(), TestListComp.TestListComp(),
           TestListCompAny.TestListCompAny(), TestMapAny.TestMapAny(), TestMapDeque.TestMapDeque(),
           TestMapList.TestMapList()]
TEST_FUNCTIONS = [FunctionExponent.FunctionExponent(),
                  FunctionLargeMath.FunctionBigMath(),
                  FunctionPygameCircle.FunctionPygameCircle(DATA_SIZE)]

print_write("DATA SIZE = " + str(DATA_SIZE))
print_write()
print_write("REPETITIONS = " + str(REPETITIONS))
print_write()


Results = [[]]
for test in TESTEES:
    Results[0].append((0, test.__class__.__name__))

for tf in range(len(TEST_FUNCTIONS)):
    print("STARTING " + str(TEST_FUNCTIONS[tf]))
    for test in TESTEES:
        print("TESTING " + str(test))
        print("Progress ", end="", flush=True)
        test.setup(TEST_FUNCTIONS[tf], DATA)
        for i in range(REPETITIONS):
            print(" " + str(i), end="", flush=True)
            test.start_time()
            test.run()
            test.end_time()
            test.reset()
        print()
        test.average_time /= REPETITIONS
    TEST_FUNCTIONS[tf].close()
    Results.append([])
    for i in range(len(TESTEES)):
        Results[0][i] = (TESTEES[i].average_time + Results[0][i][0], TESTEES[i].__class__.__name__)
        Results[-1].append((TESTEES[i].average_time, TESTEES[i].__class__.__name__))
    Results[-1].sort()

    print_write()
    print_write("### Results of Function " + TEST_FUNCTIONS[tf].__class__.__name__)
    print_write()
    print_write("|             Test             |         Average Time         |")
    print_write("|------------------------------|------------------------------|")
    for j in range(len(Results[tf+1])):
        print_write("|%-30s|%-30f|" % (Results[tf+1][j][1], Results[tf+1][j][0]))


Results[0].sort()
print_write("### Overall Results")
print_write()
print_write("|             Test             |         Average Time         |")
print_write("|------------------------------|------------------------------|")
# print(Results)
for j in range(len(Results[0])):
    # print(Results[0][j][0])
    # print(len(TEST_FUNCTIONS))
    print_write("|%-30s|%-30f|" % (Results[0][j][1], Results[0][j][0] / len(TEST_FUNCTIONS)))

