# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    number_1, number_2 = 0,0
    first_zero_1 = True if l1.val == 0 and l1.next is not None else False
    first_zero_2 = True if l2.val == 0 and l2.next is not None else False
    tail_1 = 10 if first_zero_1 else 1
    head = l1.next
    while head is not None:
        if head.val == 0:
            tail_1 = tail_1*10
        else:
            break
        head = head.next
    tail_2 = 10 if first_zero_2 else 1
    head = l2.next
    while head is not None:
        if head.val == 0:
            tail_2 = tail_2*10
        else:
            break
        head = head.next
    
    while l1 is not None:
        number_1 = number_1*10
        number_1 = number_1+l1.val
        l1 = l1.next
    while l2 is not None:
        number_2 = number_2*10
        number_2 = number_2+l2.val
        l2 = l2.next
    reverse_number_1 = 0
    while(number_1 > 0):
        reminder = number_1 %10
        reverse_number_1 = (reverse_number_1 *10) + reminder
        number_1 = number_1 //10
    if first_zero_1:
        reverse_number_1 = reverse_number_1*tail_1
    reverse_number_2 = 0
    while(number_2 > 0):
        reminder = number_2 %10
        reverse_number_2 = (reverse_number_2 *10) + reminder
        number_2 = number_2 //10
    if first_zero_2:
        reverse_number_2 = reverse_number_2*tail_2
    total = reverse_number_1 + reverse_number_2  
    head = ListNode()
    head.val = total%10
    total = total//10
    old = head
    while total > 0:
        new = ListNode()
        new.val = total%10
        new.next = None
        total = total//10
        old.next = new
        old = new
    return head

l1 = ListNode()
l1.val = 0
l2 = ListNode()
l2.val = 9
list_1 = [0,1,4,4,3,5,9,5]
list_2 = [4,0,6,1,7,8,2,1,1]
old = l1
for item in list_1:
    node = ListNode()
    node.val = item
    node.next = None
    old.next = node 
    old = node
old = l2
for item in list_2:
    node = ListNode()
    node.val = item
    node.next = None
    old.next = node 
    old = node
addTwoNumbers(l1, l2)