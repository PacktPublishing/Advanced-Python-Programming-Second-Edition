from theano import function, config
import theano.tensor as T
import numpy as np
import time

N = 5000

A_data = np.random.rand(N, N).astype('float32')
B_data = np.random.rand(N, N).astype('float32')

A = T.matrix('A')
B = T.matrix('B')

f = function([A, B], T.dot(A, B))

start = time.time()
f(A_data, B_data)

print("Matrix multiply ({}) took {} seconds".format(N, time.time() - start))
print('Device used:', config.device)
