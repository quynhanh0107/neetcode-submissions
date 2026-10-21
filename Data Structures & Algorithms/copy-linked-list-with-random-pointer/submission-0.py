"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        list1 = head
        while list1 is not None:
            list2 = Node(list1.val)
            list2.next = list1.next
            list1.next = list2
            list1 = list2.next
        newHead = head.next
        list1 = head

        while list1 is not None:
            if list1.random is not None:
                list1.next.random = list1.random.next
            list1 = list1.next.next
        list1 = head

        while list1 is not None:
            list2 = list1.next
            list1.next = list2.next
            if list2.next is not None:
                list2.next = list2.next.next
            list1 = list1.next
        return newHead


        