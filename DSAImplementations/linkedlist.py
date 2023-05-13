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
            itr = itr.next

l1 = LinkedList([2,4,3])
l2 = LinkedList([5,6,4])

