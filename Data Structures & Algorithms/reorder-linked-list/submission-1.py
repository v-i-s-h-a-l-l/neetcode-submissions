# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp = head
        arr = []
        while temp is not None:
            arr.append(temp.val)
            temp = temp.next
        arr1 = [0] * len(arr)   
        num = 0
        num1 = 1
        for i in range(len(arr)):
            if i % 2 == 0:
                arr1[i] = arr[num]
                num += 1
            else:
                arr1[i] = arr[len(arr) - num1]
                num1 += 1
        temp = head
        i = 0
        while temp:
            temp.val = arr1[i]
            i += 1
            temp = temp.next