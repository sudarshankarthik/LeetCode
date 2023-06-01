class ListNode:
    def __init__(self,value):
        self.value = value
        self.next = None

class MyHashSet:    

    def __init__(self):
        self.set = [ListNode(-1) for i in range(10000)]

    def getHash(self,value: int) -> int:
        return value % 10000

    def add(self, key: int) -> None:
        node = ListNode(key)
        hashVal = self.getHash(key)
        head = self.set[hashVal]
        while head.next:
            if head.next.value == key:
                return
            head = head.next

        head.next = node

    def remove(self, key: int) -> None:
        hashVal = self.getHash(key)
        head = self.set[hashVal]
        while head.next:
            if head.next.value == key:
                head.next = head.next.next
                return
            head = head.next

    def contains(self, key: int) -> bool:
        hashVal = self.getHash(key)
        head = self.set[hashVal]
        while head:
            if key == head.value:
                return True
            head = head.next

        return False


myHashSet = MyHashSet();
myHashSet.add(1)
myHashSet.add(2)
print(myHashSet.contains(1))
print(myHashSet.contains(3))
myHashSet.add(2)
print(myHashSet.contains(2))
myHashSet.remove(2)
print(myHashSet.contains(2))