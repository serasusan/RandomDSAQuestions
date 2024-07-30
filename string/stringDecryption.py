# push to stack till ] is encountered
# Input: s = "3[a2[c]]" Output: "accaccacc"
s = '3[a2[c]]'
stack = []
i = 0
while i<len(s):
    if s[i].isdigit():
        num = 0
        while s[i].isdigit():
            num=num*10+int(s[i])
            i+=1
        stack.append(num)
    elif s[i]=='[':
        stack.append(s[i])
        i+=1
    elif s[i]==']':
        substring = ''
        while stack and isinstance(stack[-1],str) and stack[-1]!='[':
            substring = stack.pop()+substring
        stack.pop()
        count = stack.pop()
        stack.append(substring*count)
        i+=1
    else:
        stack.append(s[i])
        i+=1
result =''.join(stack)
print(result)
        



