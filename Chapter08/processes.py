import multiprocessing
import time

class Process(multiprocessing.Process):
    def __init__(self, id):
        super(Process, self).__init__()
        self.id = id

    def run(self):
        time.sleep(1)
        print("I'm the process with id: {}".format(self.id))

def square(x):
    return x * x

def map_test():
    pool = multiprocessing.Pool()
        
    inputs = [0, 1, 2, 3, 4]
    outputs = pool.map(square, inputs)
    print(outputs)
    outputs_async = pool.map_async(square, inputs)
    outputs = outputs_async.get()
    print(outputs)


if __name__ == '__main__':
    processes = Process(1), Process(2), Process(3), Process(4)
    [p.start() for p in processes]

    map_test()
