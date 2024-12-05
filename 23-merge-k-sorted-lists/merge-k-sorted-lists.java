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
    /**
    https://leetcode.com/problems/merge-k-sorted-lists/solutions/429518/java-summary-of-all-solutions-b-f-minpq-divide-and-conquer
     */
    public ListNode mergeKLists(ListNode[] lists) {

        return mergeSort(lists, 0, lists.length-1);
        
    }

    public ListNode mergeSort (ListNode [] lists, int start, int end) {
        if (start > end) {
            return null;
        } else if (start == end) {
            return lists[start];
        } else {
            int mid = start + (end-start)/2;

            ListNode leftSorted = mergeSort(lists, start, mid);
            ListNode rightSorted = mergeSort(lists, mid + 1, end);

            ListNode mergeLeftRight = merge(leftSorted, rightSorted);
            return mergeLeftRight;
        }
    }

    private ListNode merge(ListNode left, ListNode right) {
        ListNode head = new ListNode(-1);
        ListNode p = head;

        while (left != null && right != null) {
            if (left.val <= right.val) {
                p.next = left;
                left = left.next;
            } else {
                p.next = right;
                right = right.next;
            }
            p = p.next;
        }

        while (left != null) {
            p.next = left;
            left = left.next;
            p = p.next;
        }

        while (right != null) {
            p.next = right;
            right = right.next;
            p = p.next;
        }

        return head.next;

    }
}