# Memoization

def fib(n,dp):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if dp[n] != -1:
        return dp[n]
    dp[n] = fib(n-1,dp) + fib(n-2,dp)
    return dp[n]

def main():
    print("Enter the number")
    n = int(input())
    dp = [-1] * (n+1) # Initialize the dp array with -1
    print(fib(n,dp))