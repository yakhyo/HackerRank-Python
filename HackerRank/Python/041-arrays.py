import numpy as np


def arrays(arr):
    # complete this function
    # use numpy.array
    arr = np.array(arr, dtype=np.float)
    return arr[::-1]


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
