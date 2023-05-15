class Node:
    def __init__(self,value=None,next=None) -> None:
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self,value = []):
        self.head = Node()
        if len(value) == 0:
            return
        for i in range(len(value)-1,-1,-1):
            self.insert(value[i])

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

list = LinkedList()
list.insert(3)
list.print()

