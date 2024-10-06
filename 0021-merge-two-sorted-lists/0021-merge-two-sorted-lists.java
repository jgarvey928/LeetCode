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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {

 ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        while(list1 != null && list2 != null){
           if(list1.val < list2.val){
            current.next = list1;
            list1 = list1.next;
           }
           else{
            current.next = list2;
            list2 = list2.next;
           }
           current = current.next; 
        }
        current.next= list1 != null ? list1 :list2; 
        return dummy.next;

    }

    public static void main(String args[]){
        ListNode list1 = new ListNode(1);
        list1.next = new ListNode(2);
        list1.next.next = new ListNode(2);

        ListNode list2 = new ListNode(1);
        list2.next = new ListNode(3);
        list2.next.next = new ListNode(4);

        // Test mergeTwoLists
        Solution solution = new Solution();
        ListNode mergedList = solution.mergeTwoLists(list1, list2);

    }
}