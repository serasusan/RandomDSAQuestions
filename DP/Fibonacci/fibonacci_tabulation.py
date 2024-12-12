# tabulation
def fibonacci(n,dp):
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n])
    
def main():
    print("Enter the number")
    n = int(input())
    dp = [-1]*(n+1)
    fibonacci(n,dp)

if __name__ == "__main__":
    main()