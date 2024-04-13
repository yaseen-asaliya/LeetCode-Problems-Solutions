/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }

x = x + y; // 2 + 3 =5
y = x - y; // 5 - 2 = 3 
x = x - y; // 5 - 3 = 2

 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        if(head == null || head.next == null){
            return head;
        }

        ListNode current = head, next = head.next;
        while(next != null){
            current.val = current.val + next.val;
            next.val = current.val - next.val;
            current.val = current.val - next.val;
            if(next.next == null){
                break;
            }
            current = next.next;
            next = next.next.next;
            
        }
        return head;
    }
}