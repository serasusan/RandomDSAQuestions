def printsubseq(ind,ans,s,n):
    if ind==n:
        print(''.join(ans))
        return
    ans.append(s[ind])
    printsubseq(ind+1,ans,s,n)
    ans.pop()
    printsubseq(ind+1,ans,s,n)

s="abc"
n=len(s)
printsubseq(0,[],s,n)