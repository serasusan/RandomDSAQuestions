start = 10
goal = 7
c = 0
# 1 0 1 0
# 0 1 1 1

control = min(start,goal)

while control>0 :
    print("upper outside",start, goal)
    if(start%2!=goal%2):
        print(start,goal)
        print(start%2,goal%2)
        c+=1
    start=start//2
    goal = goal//2
    control = min(start,goal)
    print("outside",start,goal)

print(c)
    
    


#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findNumberOfPartitions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findNumberOfPartitions(arr):
    # Write your code here
    n = len(arr)
    count = 0
    for i in range(1, (n//2)+1):
        for j in range(0, n-i+1):
            print("i ",i,"j ",j)
            if j==0:
                sum2 = sum(arr[j:j+i])
                print("sum2 = arr[j:j+i]",arr[j:j+i])
                sum3 = sum(arr[j+i:n])
                print("sum3 = arr[j+i:n]",arr[j+i:n])
                print("sum2%2={},sum3%2={}".format(sum2%2,sum3%2))
                if sum2%2==0:
                    if sum3%2==1:
                        count+=1
                elif sum2%2==1:
                    if sum3%2==0:
                        count+=1
                print("count : ", count)
            elif j==(n-i):
                sum1 = sum(arr[0:j])
                sum2 = sum(arr[j:j+i])
                print("sum1 = ",sum(arr[0:j]))
                print("sum2 = arr[j:j+i]",arr[j:j+i])

                print("sum1%2={} sum2%2={}".format(sum1%2,sum2%2))


                if sum1%2==0:
                    if sum2%2==1:
                        count+=1
                elif sum1%2==1:
                    if sum2%2==0:
                        count+=1
                print("count",count)

            else:
                sum1 = sum(arr[0:j])
                sum2 = sum(arr[j:j+i])
                sum3 = sum(arr[j+i:n])
                print("sum1 = ",sum(arr[0:j]))
                print("sum2 = arr[j:j+i]",arr[j:j+i])
                print("sum3 = arr[j+i:n]",arr[j+i:n])

                print("sum1%2={} sum2%2={},sum3%2={}".format(sum1%2,sum2%2,sum3%2))


                if sum1%2==0:
                    if sum2%2==1:
                        if sum3%2==0:
                            count+=1
                elif sum1%2==1:
                    if sum2%2==0:
                        if sum3%2==1:
                            count+=1
                print("count",count)
    return count
                    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = findNumberOfPartitions(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


MOD = 10**9 + 7

def findNumberOfPartitions(arr):
    n = len(arr)
    # dp[i][0] = number of ways to partition such that sum till i is even
    # dp[i][1] = number of ways to partition such that sum till i is odd
    dp = [[0, 0] for _ in range(n)]
    
    # Initial condition
    if arr[0] % 2 == 0:
        dp[0][0] = 1  # Even sum
    else:
        dp[0][1] = 1  # Odd sum
    
    for i in range(1, n):
        if arr[i] % 2 == 0:
            # If current element is even
            dp[i][0] = (dp[i-1][0] + 1) % MOD  # Extend the even partition or start a new one
            dp[i][1] = dp[i-1][1] % MOD  # Carry forward the odd partition count
        else:
            # If current element is odd
            dp[i][0] = dp[i-1][1] % MOD  # Extend the odd partition (turns even)
            dp[i][1] = (dp[i-1][0] + 1) % MOD  # Extend the even partition or start a new odd one
    
    # Sum all valid partitions
    total_partitions = (dp[-1][0] + dp[-1][1]) % MOD
    
    return total_partitions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())
    arr = [int(input().strip()) for _ in range(arr_count)]

    result = findNumberOfPartitions(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
    