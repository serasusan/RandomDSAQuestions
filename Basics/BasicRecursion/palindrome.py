def palindrome(s,i):
    if i>len(s)//2:
        return True
    if s[i]!=s[len(s)-i-1]:
        return False
    return palindrome(s,i+1)

print(palindrome("MDAM",0))