class Node:
    def __init__(self,value=None,next=None) -> None:
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self,value = []):
        if len(value) == 0:
            return
        self.head = Node(value[0])
        for i in range(1,len(value)):
            self.append(value[i])

    def len(self) -> int:
        length = 0
        itr = self.head
        while itr != None:
            length +=1
            itr = itr.next
        return length
    
    def append(self,val: int) -> None:
        itr = self.head
        while itr.next != None:
            itr = itr.next
        newNode = Node(val,None)
        itr.next = newNode
    
    def insert(self,value):
        if self.head == None:
            self.head = Node(value,None)
        newHead = Node(value,self.head)
        self.head = newHead

    def print(self) -> None:
        itr = self.head
        while itr != None:
            print(itr.value)
            itr = itr.next
    
    def valueAt(self,index: int) -> int:
        if index <= 0 or index > self.len():
            raise IndexError
        itr = self.head
        for i in range(index-1):
            itr = itr.next
        return itr.value

    def reverse(self):
        head = LinkedList()
        prvPtr = None
        cntPtr = self.head
        nxtPtr = cntPtr.next

        while nxtPtr:
            cntPtr.next = prvPtr
            prvPtr = cntPtr
            cntPtr = nxtPtr
            nxtPtr = nxtPtr.next
        cntPtr.next = prvPtr
        head.head = cntPtr
        return head
    
list = LinkedList([1,2,3,4,5])
list.insert(0)
list.insert(-1)
list.insert(-2)
listR = list.reverse()
listR.print()

