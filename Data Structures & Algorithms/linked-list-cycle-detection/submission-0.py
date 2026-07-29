# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False

        slowPtr = head
        fastPtr = head.next

        while slowPtr != fastPtr and fastPtr != None and fastPtr.next != None:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next

        if slowPtr == fastPtr:
            return True
        else:
            return False