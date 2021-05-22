# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1   
        head = ListNode()
        if l1.val < l2.val:
            head.val = l1.val
            l1 = l1.next
        else:
            head.val = l2.val
            l2 = l2.next
        start = head
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                current = ListNode()
                current.val = l1.val
                start.next = current
                start = start.next
                l1 = l1.next
            else:
                current = ListNode()
                current.val = l2.val
                start.next = current
                start = start.next
                l2 = l2.next
        while l1 is not None:
            current = ListNode()
            current.val = l1.val
            start.next = current
            start = start.next
            l1 = l1.next
        while l2 is not None:
            current = ListNode()
            current.val = l2.val
            start.next = current
            start = start.next
            l2 = l2.next
        return head