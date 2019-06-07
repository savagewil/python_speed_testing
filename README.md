# python_speed_testing
Will provide an architecture for speed testing for different python components

# One Example of a Test
DATA SIZE = 1000

REPETITIONS = 20

### Overall Results

|             Test             |         Average Time         |
|------------------------------|------------------------------|
|TestListCompAny               |0.005064                      |
|TestMapDeque                  |0.005198                      |
|TestMapList                   |0.005219                      |
|TestForLoop                   |0.005273                      |
|TestMapAny                    |0.005380                      |
|TestListComp                  |0.005598                      |
|TestForLoopListAppend         |0.005896                      |
|TestForLoopListAppend         |0.006070                      |

### Results of Function FunctionExponent

|             Test             |         Average Time         |
|------------------------------|------------------------------|
|TestListCompAny               |0.009294                      |
|TestForLoop                   |0.009375                      |
|TestMapAny                    |0.009494                      |
|TestMapDeque                  |0.009494                      |
|TestMapList                   |0.009609                      |
|TestListComp                  |0.009644                      |
|TestForLoopListAppend         |0.010644                      |
|TestForLoopListAppend         |0.011313                      |

### Results of Function FunctionBigMath

|             Test             |         Average Time         |
|------------------------------|------------------------------|
|TestMapDeque                  |0.002498                      |
|TestMapList                   |0.002548                      |
|TestListCompAny               |0.002648                      |
|TestForLoop                   |0.002698                      |
|TestListComp                  |0.002998                      |
|TestForLoopListAppend         |0.003098                      |
|TestForLoopListAppend         |0.003148                      |
|TestMapAny                    |0.003198                      |

### Results of Function FunctionPygameCircle

|             Test             |         Average Time         |
|------------------------------|------------------------------|
|TestListCompAny               |0.003249                      |
|TestMapAny                    |0.003448                      |
|TestMapList                   |0.003498                      |
|TestMapDeque                  |0.003602                      |
|TestForLoop                   |0.003746                      |
|TestForLoopListAppend         |0.003749                      |
|TestForLoopListAppend         |0.003946                      |
|TestListComp                  |0.004152                      |
