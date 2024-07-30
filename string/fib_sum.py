def fib(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
def fiblistGen(k):
    #generate list of fib numbers less than k
    fiblist = []
    i = 0
    while(fib(i)<k):
        fiblist.append(fib(i))
        i+=1
    return fiblist


# call this recursively
def findCount(count,k,fiblist):
    if k in fiblist:
        count += 1
        # print(count,"count")
    else:
        #find the value just less than k
        i = 0
        while fiblist[i]<k:
            i += 1
        fiblist = fiblist[:i]
        length = len(fiblist)
        firstval = fiblist[length-1]
        # print("firstval",firstval)
        count+=1
        j = k - firstval
        
        count = findCount(count,j,fiblist)
    # print("count outside",count)
    return count



def getInput(k):
    l = 109
    fiblist = fiblistGen(l)
    count = 0
    return findCount(count,k,fiblist)

