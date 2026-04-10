import numpy as np
def is_prime(x):
    for i in range(2, x - 1):
        if x % i == 0:
            return False
    return True
 
print(is_prime(10))
primi = np.array([i for i in range(10) if is_prime(i)])
primi
 
primi = np.array([2, 3, 5, 7])
print(len(primi))
primi.size
primi.dtype
 