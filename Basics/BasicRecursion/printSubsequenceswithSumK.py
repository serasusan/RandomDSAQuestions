# def printsubseq(ind,ans,s,n,sum,k):
#     if ind==n:
#         if sum==k:
#             print(ans)
#         return
#     ans.append(s[ind])
#     sum += s[ind]
#     printsubseq(ind+1,ans,s,n,sum,k)
#     ans.pop()
#     sum -= s[ind]
#     printsubseq(ind+1,ans,s,n,sum,k)

# s=[1,2,1]
# n=len(s)
# printsubseq(0,[],s,n,0,2)

# 
def printsubseq(ind,ans,s,n,sum,k):
    if ind==n:
        if sum==k:
            print(ans)
            return True
        return False
    ans.append(s[ind])
    sum += s[ind]
    if printsubseq(ind+1,ans,s,n,sum,k)==True:
        return True
    ans.pop()
    sum -= s[ind]
    if printsubseq(ind+1,ans,s,n,sum,k)==True:
        return True

s=[1,2,1]
n=len(s)
printsubseq(0,[],s,n,0,2)