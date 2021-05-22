# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists) -> ListNode:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        total_list = []
        all_node = True
        for list in lists:
            if list is not None:
                all_node = False
            while list is not None:
                total_list.append(list.val)
                list = list.next
        if all_node:
            return None
        total_list.sort()
        head = ListNode
        node = None
        for item in total_list:
            if node is None:
                head.val = item
                node = head
            else:
                temp = ListNode()
                temp.val = item
                node.next = temp
                node = node.next
        return head

node = ListNode()
node.val = 1
result = mergeKLists([None, node])
print(result)