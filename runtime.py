import numpy as np
import time

arr = np.random.randn(100, 100)
arr = arr * 1000000000000000000    ##########################
arr.dtype = 'float64'       ##########################
print(arr.dtype)
time_start = time.time()
for i in range(500):
    for j in range(500):
        arr * arr
    print(i)
time_end = time.time()
time_mul = time_end - time_start
print('time cost', time_end - time_start, 's')

# arr = np.random.randn(100, 100)
# arr = arr * 32767
# arr.dtype = 'int16'
print(arr.dtype)
time_start = time.time()
for i in range(500):
    for j in range(500):
        arr + arr
    print(i)
time_end = time.time()
time_pls = time_end - time_start
print('time cost', time_end - time_start, 's')

print('乘法时间：', time_mul)
print('加法时间：', time_pls)
