# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        arr1 = []
        arr2 = []

        temp = l1
        while temp:
            arr1.append(temp.val)
            temp = temp.next

        temp = l2
        while temp:
            arr2.append(temp.val)
            temp = temp.next

        carry = 0
        arr3 = []

        n = max(len(arr1), len(arr2))

        for i in range(n):
            val1 = arr1[i] if i < len(arr1) else 0
            val2 = arr2[i] if i < len(arr2) else 0

            total = val1 + val2 + carry

            arr3.append(total % 10)
            carry = total // 10

        if carry:
            arr3.append(carry)

        # Convert array to linked list
        dummy = ListNode()
        current = dummy

        for num in arr3:
            current.next = ListNode(num)
            current = current.next

        return dummy.next