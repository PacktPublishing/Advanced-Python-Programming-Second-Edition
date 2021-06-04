import numpy as np
from distance import chebyshev

def benchmark():
     a = np.random.rand(1000, 2)
     b = np.random.rand(1000, 2)
     for x1, y1 in a:
        for x2, y2 in b:
            chebyshev(x1, x2, y1, y2)

if __name__ == '__main__':
    benchmark()
