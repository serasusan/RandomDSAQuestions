def printsubseq(ind,ans,s,n,sum,k):
    if sum>k:
        return 0
    if ind==n:
        if sum==k:
            return 1
        return 0
    ans.append(s[ind])
    sum += s[ind]
    l = printsubseq(ind+1,ans,s,n,sum,k)
    ans.pop()
    sum -= s[ind]
    r = printsubseq(ind+1,ans,s,n,sum,k)
    return l+r

s=[1,2,1]
n=len(s)
print("The count of subsequences with Sum 2 from array [1,2,1] is",printsubseq(0,[],s,n,0,2))

