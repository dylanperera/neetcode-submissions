class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyHashSet:

    def __init__(self):
       self.hash_set = [None] * 13337
        
    def add(self, key: int) -> None:
        bucket = key % 13337

        if self.hash_set[bucket] is None:
            self.hash_set[bucket] = Node(key)
        else:
            currPtr = self.hash_set[bucket]

            while currPtr.next != None:
                if currPtr.value == key:
                    return

                currPtr = currPtr.next

                currPtr.next = Node(key)
        

    def remove(self, key: int) -> None:
        if self.hash_set[key] == None:
            return
        
        head = self.hash_set[key]

        if head.value == key:
            self.hash_set[key] = head.next
            head.next = None
        else:
            currPtr = head
            while currPtr.next != key:
                currPtr = currPtr.next

            if currPtr.next.next == None:
                currPtr.next = None
            else:
                currPtr.next = currPtr.next.next

    def contains(self, key: int) -> bool:
        if self.hash_set[key] is not None:
            currPtr = self.hash_set[key]

            while currPtr != None:
                if currPtr.value == key:
                    return True

                currPtr = currPtr.next

        return False






# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(2)
# print(obj.contains(3))
# obj.remove(key)
# param_3 = obj.contains(key)