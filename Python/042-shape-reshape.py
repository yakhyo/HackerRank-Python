import numpy as np

a = list(map(int, input().split()))
arr = np.array(a)
arr = np.reshape(arr,(3, 3))
print(arr)
