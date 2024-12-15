class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ''
        for i in range(len(s)):
            if s[i].isalnum():
                newstr += s[i].lower()
        n = len(newstr)
        for i in range(n):
            if newstr[i]!=newstr[n-i-1]:
                return False
        return True
    

class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        l,r = 0, n-1

        while l<r:
            while l<r and not self.alnum(s[l]): # I can also use s[l].isalnum()
                l+=1
            while l<r and not self.alnum(s[r]):
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l,r = l+1, r-1
        return True

    def alnum(self,c):
        return(ord('A') <= ord(c) <= ord('Z') or
               ord('a') <= ord(c) <= ord('z') or
               ord('0') <= ord(c) <= ord('9'))
    