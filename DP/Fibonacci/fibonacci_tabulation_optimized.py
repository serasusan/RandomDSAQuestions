def fib(n,dp):
    prev2 = 0
    prev = 1
    for i in range(2,n+1):
        curr = prev2+prev
        prev2 = prev
        prev = curr
    print("Fibanocci of",n,"is",curr)


if __name__ == "__main__":
    print("Enter the number")
    n = int(input())
    dp = [-1]*(n+1)
    fib(n,dp)