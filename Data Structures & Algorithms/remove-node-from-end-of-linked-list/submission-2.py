# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
# Nth from end → two pointers → fixed gap → dummy → left lands BEFORE target → skip target.
        dummy = ListNode(0)
        dummy.next = head

        left = right = dummy

        # 1. Advance the 'right' pointer n + 1 steps
        for _ in range(n + 1):
            right = right.next

        # 2. Move both pointers forward until 'right' hits the end (None)
        while right is not None:
            left = left.next
            right = right.next

        left.next = left.next.next

        return(dummy.next)



