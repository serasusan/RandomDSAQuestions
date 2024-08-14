# given a sorted array, find the count of pairs that add upto the value k

def count_pairs(arr, k):
    # there are 2 pointers, start and end
    #[1,4,4,5,5,5,6,6,11] k=10
    n = len(arr)
    start = 0
    end = n-1
    count = 0
    while end>start:
        sum = arr[start]+arr[end]
        if sum<k:
            start += 1
        elif sum>k:
            end += 1
        else:
            if arr[start]!=arr[end]:
                c1 = 1
                c2 = 1
                while arr[start]==arr[start+1] and start+1<end:
                    c1 +=1
                    start+=1
                while arr[end]==arr[end+1] and start<end-1:
                    c2+=1
                    end-=1
                count += c1*c2
            else:
                c3 = 0
                c3 = end-start+1
                # apply combination here
                # c3C2
                count += (c3*(c3-1))//2
                break
