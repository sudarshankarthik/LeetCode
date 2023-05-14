class Node:
    def __init__(self,value = None,next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self,value = []):
        self.head = Node()
        if len(value) == 0:
            return
        for i in range(len(value)-1,-1,-1):
            self.insert(value[i])


    def insert(self,value):
        newHead = Node(value,self.head)
        self.head = newHead

    def print(self):
        itr = self.head
        while(itr.next != None):
            print(itr.value)
            itr = itr.nextṭ

l1 = LinkedList([2,4,3])
l2 = LinkedList([5,6,4])




def to_Num(l1: LinkedList) -> int:
    num = 0
    itr = l1
to_Num(l1)


################################################################
################################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def toNum(self,ln: ListNode):
        itr = ln
        num = 0
        placeValue = 1
        while(itr != None):
            num += itr.val*placeValue
            placeValue *= 10
            itr = itr.next
        return num
    def toList(self,n: int):
        l = ListNode()
        while(n != 0):
            nd = ListNode(n%10,l)
            l = nd
            n //= 10
        return l
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n = self.toNum(l1) + self.toNum(l2)
        return self.toList(n)
