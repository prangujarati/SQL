class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node. This simplifies the process of merging.
        dummy = ListNode()
        current = dummy  # This will point to the current node in the merged list

        # Traverse through both lists and compare the values
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1  # Attach the smaller node to the merged list
                list1 = list1.next  # Move the pointer to the next node in list1
            else:
                current.next = list2  # Attach the smaller node to the merged list
                list2 = list2.next  # Move the pointer to the next node in list2

            current = current.next  # Move the pointer to the last added node in the merged list

        # If any nodes remain in list1 or list2, append them to the merged list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # Return the merged list (skip the dummy node)
        return dummy.next
