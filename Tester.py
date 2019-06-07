import time

from Testees import TestForLoop, TestForLoopListAppend, TestForLoopListPrebuilt
from Testees import TestListComp, TestListCompAny, TestMapAny, TestMapDeque, TestMapList

from TestingFunctions import FunctionExponent, FunctionLargeMath, FunctionPygameCircle


DATA_SIZE = 5000
REPETITIONS = 100
DATA = list(range(DATA_SIZE))

TESTEES = [TestForLoop.TestForLoop(), TestForLoopListAppend.TestForLoopListAppend(),
           TestForLoopListPrebuilt.TestForLoopListAppend(), TestListComp.TestListComp(),
           TestListCompAny.TestListCompAny(), TestMapAny.TestMapAny(), TestMapDeque.TestMapDeque(),
           TestMapList.TestMapList()]
TEST_FUNCTIONS = [FunctionExponent.FunctionExponent(),
                  FunctionLargeMath.FunctionBigMath(),
                  FunctionPygameCircle.FunctionPygameCircle(DATA_SIZE)]

Results = [[]]
for test in TESTEES:
    Results[0].append((0, test.__class__.__name__))

for test_func in TEST_FUNCTIONS:
    for test in TESTEES:
        test.setup(test_func, DATA)
        for i in range(REPETITIONS):
            test.start_time()
            test.run()
            test.end_time()
            test.reset()
        test.average_time /= REPETITIONS
    test_func.close()
    Results.append([])
    for i in range(len(TESTEES)):
        Results[0][i] = (TESTEES[i].average_time + Results[0][i][0], TESTEES[i].__class__.__name__)
        Results[-1].append((TESTEES[i].average_time, TESTEES[i].__class__.__name__))
    Results[-1].sort()

print("DATA SIZE = " + str(DATA_SIZE))
print("REPETITIONS = " + str(REPETITIONS))
print()
Results[0].sort()
print("Overall Results")
print("|             Test             |         Average Time         |")
# print(Results)
for j in range(len(Results[0])):
    # print(Results[0][j][0])
    # print(len(TEST_FUNCTIONS))
    print("|%-30s|%-30f|" % (Results[0][j][1], Results[0][j][0] / len(TEST_FUNCTIONS)))

for i in range(len(TEST_FUNCTIONS)):
    print("Results of Function " + TEST_FUNCTIONS[i].__class__.__name__)
    print("|             Test             |         Average Time         |")
    for j in range(len(Results[i+1])):
        print("|%-30s|%-30f|" % (Results[i+1][j][1], Results[i+1][j][0]))
