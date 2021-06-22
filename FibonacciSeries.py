# FibonacciSeries.py
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


print('These are all the Fibonacci numbers until 1000:')
fib(1000)

