# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ptrK = ptrF = ptrL = head
        for i in range(k-1):
            ptrK = ptrK.next
            ptrL = ptrL.next

        while(ptrL.next != None):
            ptrF = ptrF.next
            ptrL = ptrL.next

        ptrK.val,ptrF.val = ptrF.val,ptrK.val
        return head
    