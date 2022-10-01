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
    public int pairSum(ListNode head) {
        int arr[] = new int[100000];
        int n = 0;
        int maxSum = Integer.MIN_VALUE;
        
        while(head != null) {
            arr[n++] = head.val;
            head = head.next;
        }

        for(int i = 0; i <= (n/2)-1; ++i) {
            if(arr[i] + arr[n-1-i] > maxSum)
                maxSum = arr[i] + arr[n-1-i];
        }

        return maxSum;

    }
}
