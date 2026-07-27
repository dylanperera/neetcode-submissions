# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Possible inputs: 
        # 1. Empty list
        # 2. 1 
        # 3. 1 -> 2 
        # 4. 1 -> 2 -> 3
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # If the list is empty or just one element, return as is
        if head == None or head.next == None:
            return head
            
        # Have 3 pointers: prev, curr, next
        prev = None
        curr = head

        # Continue this until curr.next = None
        while curr != None:
            nextN = curr.next
            curr.next = prev
            prev = curr
            curr = nextN

        return prev 



