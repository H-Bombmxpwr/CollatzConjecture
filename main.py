import math

def collatz(n):
    c = 0
    if (n<0):
        n = -1*n
    while n > 1:
        print(n, end=' , ')
        c = c + 1
        if (n % 2):
            # n is odd
            n = 3 * n + 1
        else:
            # n is even
            n = n // 2
    print(1)
    return c

n = int(input('Enter Integer = '))
print('Sequence: ', end='')
c = collatz(n)
print("Calculations =", c)