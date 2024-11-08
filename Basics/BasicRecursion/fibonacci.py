def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)

print(fib(5))

# fibonacci series - 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610