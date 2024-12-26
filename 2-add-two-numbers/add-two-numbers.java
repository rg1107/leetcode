/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode();
        ListNode temp = head;
        int sum = 0;
        int carry = 0;

        while (l1 != null && l2 != null) {
            sum = l1.val + l2.val + carry;
            carry = sum/10;
            sum = sum%10;
            ListNode digit = new ListNode(sum);
            temp.next = digit;
            temp = temp.next;
            l1 = l1.next;
            l2 = l2.next; 
        }

        ListNode t2 = l1 != null ? l1 : l2;
        while (t2 != null) {
            sum = t2.val + carry;
            carry = sum/10;
            sum = sum%10;
            ListNode digit = new ListNode(sum);
            temp.next = digit;
            temp = temp.next;
            t2 = t2.next;
        }

        if (carry > 0) {
            ListNode digit = new ListNode(carry);
            temp.next = digit;
            temp = temp.next;
        }

        return head.next;
    }
}