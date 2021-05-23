class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup( head: ListNode, k: int) -> ListNode:
        if head is None:
            return None
        list = []
        return_head = None
        next = head
        last = None
    
        while next is not None:
            list.append(next)
            next = next.next
            if len(list) == k:
                list.reverse()
                for index in range(0,len(list)-1):
                    list[index].next = list[index+1]
                if last is None:
                    return_head = list[0]
                    last = list[len(list)-1]
                    last.next = next
                else:
                    list[len(list)-1].next = next
                    last.next = list[0]
                last = list[len(list)-1]
                list = []
        return return_head

list = [1,2,3,4,5]
head = ListNode()
head.val = list.pop(0)
point = head
while len(list) != 0:
    node = ListNode()
    node.val = list.pop(0)
    point.next = node
    point = point.next
reverseKGroup(head, 2)