# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode(-1)
        temp = head

        while l1 and l2:
            s = l1.val + l2.val + carry
            carry = s//10
            node = ListNode(s % 10)
            temp.next = node
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            s = l1.val + carry
            carry = s//10
            node = ListNode(s % 10)
            temp.next = node
            temp = temp.next
            l1 = l1.next
        
        while l2:
            s = l2.val + carry
            carry = s//10
            node = ListNode(s % 10)
            temp.next = node
            temp = temp.next
            l2 = l2.next
        
        if carry > 0:
            node = ListNode(carry)
            temp.next = node
            temp = temp.next
        
        return head.next

