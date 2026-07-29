# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Input: Two linked lists of integers between -100 and 100
    # Output: Merged linked list of the two inputs
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Consider edge cases:
        # 1. One input is empty
        # 2. Both inputs are empty
        if list1 == None:
            return list2
        
        if list2 == None:
            return list1

        ptr1Prev = ListNode(0, list1)
        head = ptr1Prev
        ptr1 = list1
        ptr2 = list2

        while ptr1 != None and ptr2 != None:
            # Compare pointer values
            if ptr2.val <= ptr1.val:
                # insert infront of previous
                ptr1Prev.next = ListNode(ptr2.val, ptr1Prev.next)
                # move ptr2 up
                ptr2 = ptr2.next
                # move the previous pointer up
                ptr1Prev = ptr1Prev.next
            else:
                # move ptr1 up
                ptr1 = ptr1.next
                # move previous pointer up
                ptr1Prev = ptr1Prev.next

        if ptr2 != None:
            while ptr2 != None:
                ptr1Prev.next = ListNode(ptr2.val, ptr1Prev.next)
                # move ptr2 up
                ptr2 = ptr2.next
                # move the previous pointer up
                ptr1Prev = ptr1Prev.next

        return head.next
                

                


        