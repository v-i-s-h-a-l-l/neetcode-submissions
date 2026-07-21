# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
        arr1=arr[::-1]
        i=0
        temp=head
        while temp:
            temp.val=arr1[i]
            i+=1
            temp=temp.next
        return head
        
        