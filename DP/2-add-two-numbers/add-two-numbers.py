# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = curr = None

        while l1 or l2 or carry:
            v1 = getattr(l1, 'val', 0) 
            v2 = getattr(l2, 'val', 0)
            total = v1 + v2 + carry
            node = ListNode(total % 10)
            if head is None:
                head = curr = node
            else:
                curr.next = node
                curr = node


            l1 = getattr(l1, 'next', None)
            l2 = getattr(l2, 'next', None)
            carry = total // 10
        
        return head


        