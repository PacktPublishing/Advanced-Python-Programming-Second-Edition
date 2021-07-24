import multiprocessing
import random

samples = 10000000

def pi_serial():
    hits = 0

    for i in range(samples):
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(-1.0, 1.0)
    
        if x**2 + y**2 <= 1:
            hits += 1

    pi = 4.0 * hits/samples
    return pi

def sample():
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    
    if x**2 + y**2 <= 1:
        return 1
    else:
        return 0

def pi_apply_async():
    pool = multiprocessing.Pool()
    results_async = [pool.apply_async(sample) 
                     for i in range(samples)]
    hits = sum(r.get() for r in results_async)

    pi = 4.0 * hits/samples
    return pi

def sample_multiple(samples_partial):
    return sum(sample() for i in range(samples_partial))

def pi_apply_async_chunked():
    ntasks = 10
    chunk_size = samples/ntasks
    pool = multiprocessing.Pool()
    results_async = [pool.apply_async(sample_multiple, [chunk_size]) 
                     for i in range(ntasks)]
    hits = sum(r.get() for r in results_async)

    pi = 4.0 * hits/samples
    return pi
