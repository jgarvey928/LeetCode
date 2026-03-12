# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            # Get values from the nodes if they exist, otherwise use 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate total and new carry
            total = val1 + val2 + carry
            carry = total // 10
            
            # Add the digit to the new linked list
            current.next = ListNode(total % 10)
            
            # Move pointers forward
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        return dummy.next