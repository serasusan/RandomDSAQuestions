# Definition of doubly linked list:
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def deleteKthElement(self, head, k):
        if head is None:
            return None
        if k==1:
            temp  = head
            head = head.next
            head.prev = None
            del temp
            return head
        i = 1
        temp = head
        while temp is not None and i<k:
            temp = temp.next
            i+=1
        if temp is None:
            return head
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.prev = None
        temp.next = None
        del temp
        return head
    
s = Solution()
s.deleteKthElement()
