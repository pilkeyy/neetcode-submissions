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
    public ListNode reverseList(ListNode head) {
        ListNode previous = null;
        ListNode nextNode;
        ListNode curr = head;
        while(curr!= null){
            nextNode = curr.next;
            curr.next = previous;
            previous = curr;
            curr = nextNode;
        }
        return previous;
    }
}
