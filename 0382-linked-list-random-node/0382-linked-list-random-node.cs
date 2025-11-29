/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    private ListNode list;
    private int len = 0;
    private Random rand = new Random();

    public Solution(ListNode head) {
        list = head;

        ListNode t = head;
        while (t != null) {
            len++;
            t = t.next;
        }
    }

    public int GetRandom() {
        int index = rand.Next(0, len);

        ListNode t = list;
        while (index > 0) {
            t = t.next;
            index--;
        }

        return t.val;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.GetRandom();
 */