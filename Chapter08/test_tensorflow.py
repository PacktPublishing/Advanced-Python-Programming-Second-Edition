import tensorflow as tf
import numpy as np
import time
import sys

NUM_THREADS = int(sys.argv[1])
N = 30000

print('Num threads', NUM_THREADS)
x_data = np.random.uniform(-1, 1, N)
y_data = np.random.uniform(-1, 1, N)

x = tf.placeholder('float64', name='x')
y = tf.placeholder('float64', name='y')

hit_tests = x ** 2 + y ** 2 < 1.0
hits = tf.reduce_sum(tf.cast(hit_tests, 'int32'))

with tf.Session(config=tf.ConfigProto(inter_op_parallelism_threads=NUM_THREADS,
                                      intra_op_parallelism_threads=NUM_THREADS)) as sess:
    start = time.time()
    for i in range(10000):
        sess.run(hits, {x: x_data, y: y_data})
    print(time.time() - start)
