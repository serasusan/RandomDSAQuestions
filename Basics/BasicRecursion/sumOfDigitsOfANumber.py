class Solution:
    def addDigits(self, num):
        #your code goes here
        res = 0
        while(num>0):
            res += num%10
            num = num//10
        if res>9:
            return self.addDigits(res)
    
        return res


s = Solution()
print(s.addDigits(529))