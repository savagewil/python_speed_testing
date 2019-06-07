DATA_SIZE = 40000
REPETITIONS = 250
RETURN = False
from Testees import TestForLoop, TestForLoopListAppend, TestForLoopListPrebuilt
from Testees import TestListComp, TestListCompAny, TestMapAny, TestMapDeque, TestMapList

from TestingFunctions import FunctionExponent, FunctionLargeMath, FunctionPygameCircle, FunctionSigmoid, \
    FunctionSquared, FunctionExample


# from TestingFunctions import
def file_exists(file_name):
    try:
        x = open(file_name, 'r')
        x.close()
        return True
    except Exception:
        return False


data_file_index = 0
data_file = "./Results"+"/Returning" if RETURN else "" +"/result_%d_%d_%d.md" % (DATA_SIZE, REPETITIONS, data_file_index)
while file_exists(data_file):
    data_file_index += 1
    data_file = "./Results/result_%d_%d_%d.md" % (DATA_SIZE, REPETITIONS, data_file_index)

OUT_FILE = open(data_file, 'w')


def print_write(string=""):
    print(string)
    OUT_FILE.write(string + "\n")


DATA = list(range(DATA_SIZE))
if not RETURN:
    TESTEES = [TestForLoop.TestForLoop(),
               TestListComp.TestListComp(),
               TestMapAny.TestMapAny(),
               TestMapDeque.TestMapDeque(),
               TestMapList.TestMapList()]
else:
    TESTEES = [TestListComp.TestListComp(),
               TestMapList.TestMapList()]

TEST_FUNCTIONS = [FunctionLargeMath.FunctionBigMath(),
                  FunctionPygameCircle.FunctionPygameCircle(DATA_SIZE),
                  FunctionSigmoid.FunctionSigmoid(),
                  FunctionSquared.FunctionSquared(),
                  FunctionExample.FunctionExample()]

print_write("DATA SIZE = " + str(DATA_SIZE))
print_write()
print_write("REPETITIONS = " + str(REPETITIONS))
print_write()

Results = [[]]
for test in TESTEES:
    Results[0].append((0, test.__class__.__name__))
#                       Warm up
print("Warming Up")
tf = len(TEST_FUNCTIONS) - 1
average = 0
for test in TESTEES:
    test.setup(TEST_FUNCTIONS[tf], DATA, return_out=RETURN)
    for i in range(REPETITIONS):
        test.start_time()
        test.run()
        test.end_time()
        test.reset()
    test.average_time /= REPETITIONS
    average += test.average_time
average /= len(TESTEES)

# -------------------------------------------------


for tf in range(len(TEST_FUNCTIONS)):
    print("STARTING " + str(TEST_FUNCTIONS[tf]))
    average = 0
    for test in TESTEES:
        print("TESTING " + str(test))
        print("Progress ", end="", flush=True)
        test.setup(TEST_FUNCTIONS[tf], DATA, return_out=RETURN)
        for i in range(REPETITIONS):
            print(" " + str(i), end="", flush=True)
            test.start_time()
            test.run()
            test.end_time()
            test.reset()
        print()
        test.average_time /= REPETITIONS
        average += test.average_time
    average /= len(TESTEES)
    TEST_FUNCTIONS[tf].close()
    Results.append([])
    for i in range(len(TESTEES)):
        Results[0][i] = (TESTEES[i].average_time / average + Results[0][i][0], TESTEES[i].__class__.__name__)
        Results[-1].append((TESTEES[i].average_time, TESTEES[i].__class__.__name__))
    Results[-1].sort()

    print_write()
    print_write("### Results of Function " + TEST_FUNCTIONS[tf].__class__.__name__)
    print_write()
    print_write("|             Test             |      Average Time (sec)      |")
    print_write("|------------------------------|------------------------------|")
    for j in range(len(Results[tf + 1])):
        print_write("|%-30s|%-30f|" % (Results[tf + 1][j][1], Results[tf + 1][j][0]))

Results[0].sort()
print_write("### Overall Results")
print_write()
print_write("|             Test             |    Average Score (sec/sec)   |")
print_write("|------------------------------|------------------------------|")
# print(Results)
for j in range(len(Results[0])):
    # print(Results[0][j][0])
    # print(len(TEST_FUNCTIONS))
    print_write("|%-30s|%-30f|" % (Results[0][j][1], Results[0][j][0] / len(TEST_FUNCTIONS)))
