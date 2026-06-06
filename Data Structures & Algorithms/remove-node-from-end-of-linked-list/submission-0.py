# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr=[]
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
        arr.pop(-n)
        if not arr:
            return None
        
        temp=head
        i=0
        while i < len(arr):
            temp.val=arr[i]
            i=i+1
            prev=temp
            temp=temp.next
        prev.next=None

        return head
        