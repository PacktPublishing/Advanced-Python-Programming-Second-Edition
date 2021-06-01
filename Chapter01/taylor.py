def factorial(n): 
    if n == 0: 
        return 1.0 
    else: 
        return float(n) * factorial(n-1) 

def taylor_exp(n): 
    return [1.0/factorial(i) for i in range(n)] 

def taylor_sin(n): 
    res = [] 
    for i in range(n): 
        if i % 2 == 1: 
           res.append((-1)**((i-1)/2)/float(factorial(i))) 
        else: 
           res.append(0.0) 
    return res 

def benchmark(): 
    taylor_exp(500) 
    taylor_sin(500) 

if __name__ == '__main__': 
    benchmark() 
