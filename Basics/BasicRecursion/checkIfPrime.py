class Solution:
    def checkPrime(self, num):
        n = 0
        def count(num,i):
            nonlocal n
            if n>2:
                return False
            if i==num+1:
                return True
            if num%i==0:
                n+=1
            return count(num,i+1)
        
        return count(num,1)

s = Solution()
print(s.checkPrime(13))