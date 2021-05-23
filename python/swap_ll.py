# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head: ListNode) -> ListNode:
        if head is None:
            return None
        
        slow = head
        fast = None if head.next is None else head.next
        if fast is None:
            return head
        fast_next = fast.next
        fast.next = slow
        slow.next = fast_next
        slow, fast = fast, slow
        index = 0
        head = slow
        parent = head 
        while fast is not None:
            slow, fast = fast, fast.next
            if index > 0:
                parent = parent.next
            index += 1
            if index%2 == 0 and fast is not None:
                fast_next = fast.next
                if fast_next is None:
                    fast.next = slow
                parent.next = fast
                fast.next = slow
                slow.next = fast_next
                slow, fast = fast, slow
        return head

list = [1,2,3,4,5]
head = ListNode()
head.val = list.pop(0)
point = head
while len(list) != 0:
    node = ListNode()
    node.val = list.pop(0)
    point.next = node
    point = point.next

swapPairs(head)