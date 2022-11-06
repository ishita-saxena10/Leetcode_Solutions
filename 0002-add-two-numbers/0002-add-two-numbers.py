# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a1=""
        a2=""
        while l1:
            a1+=(str(l1.val))
            l1=l1.next
        while l2:
            a2+=(str(l2.val))
            l2=l2.next
        aa1=a1[::-1]
        aa2=a2[::-1]
        s=str(int(aa1)+int(aa2))
        s1=list(s[::-1])
        print (s1)
        head=l=ListNode()
        for i in s1:
            l.next=ListNode(i)
            l=l.next
        return head.next