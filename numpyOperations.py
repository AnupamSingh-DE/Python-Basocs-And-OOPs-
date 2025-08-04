# Append insert Delete

import numpy as np

arr = np.array([1,2,3])
print(arr)
np.append([1,2,3],[[1,21,23],[11,21,25]],0)
print(arr)
newarr = arr.reshape(3,3)

print(newarr)