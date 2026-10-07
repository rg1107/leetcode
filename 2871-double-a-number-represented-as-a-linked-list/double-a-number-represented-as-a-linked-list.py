# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        carry = self.rec(head)

        if carry > 0:
            node = ListNode(carry)
            node.next = dummy.next
            dummy.next = node
        
        return dummy.next
    

    def rec(self, node) -> int:
        if not node:
            return 0
        
        prev_carry = self.rec(node.next)
        mul = node.val * 2 + prev_carry
        carry = mul // 10
        node.val = mul % 10
        return carry



        