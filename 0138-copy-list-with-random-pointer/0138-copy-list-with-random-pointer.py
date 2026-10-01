"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head):
        if head is None:
            return None

        copies = {}

        curr = head

        # Create copies
        while curr:
            copies[curr] = Node(curr.val)
            curr = curr.next

        # Connect pointers
        curr = head

        while curr:
            copies[curr].next = copies.get(curr.next)
            copies[curr].random = copies.get(curr.random)
            curr = curr.next

        return copies[head]