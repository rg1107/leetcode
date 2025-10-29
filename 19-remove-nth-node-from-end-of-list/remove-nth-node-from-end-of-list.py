# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        
        temp = head
        for _ in range(n):
            temp = temp.next

        slow = head
        if not temp:
            return head.next
            
        while temp.next:
            slow = slow.next
            temp = temp.next
        
        if slow.next:
            slow.next = slow.next.next
        
        return head

