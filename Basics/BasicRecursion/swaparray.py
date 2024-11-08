def swapArray(arr,l,r):
    if l<r:
        arr[l],arr[r]=arr[r],arr[l]
        swapArray(arr,l+1,r-1)

A = [1,2,3,4,5]
swapArray(A,0,4)
print(A)