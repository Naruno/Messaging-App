from random import randint
from math import log2


def is_prime(n):
    """
    is_prime(n) - Miller-Rabin primality test for integer n > 3
    Uses random.randint, math.log2
    """
    assert n > 3
    k = 20 #int(log2(n))
    m = n - 1
    d = 0
    while(m % 2 == 0):
        m //= 2
        d += 1
    for _ in range(k):
        a = randint(2, n - 2)
        x = pow(a, m, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(d - 1):
            x = pow(x, 2, n)
            if x == 1:
                return 0
            if x == n - 1:
                break
        if x != n - 1:
            return 0
    return 1


def main():
    print('Probably prime' if is_prime(int(input('Number:')))
        else 'Composite')
        
if __name__ == "__main__":
    main()