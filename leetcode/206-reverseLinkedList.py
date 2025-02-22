"""
https://leetcode.com/problems/reverse-linked-list/description/
"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current 
            current = temp
        return prev

# time: O(n)
# space: O(1)
