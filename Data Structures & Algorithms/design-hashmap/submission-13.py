class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.hash_map = [None] * 13337

    def put(self, key: int, value: int) -> None:
        bucket = key % 13337

        if self.hash_map[bucket] == None:
            self.hash_map[bucket] = Node(key, value)
        else:
            currPtr = self.hash_map[bucket]

            if currPtr.key == key:
                currPtr.value = value
                return

            while currPtr.next != None:
                
                if currPtr.key == key:
                    currPtr.value = value
                    return

                currPtr = currPtr.next

                currPtr.next = Node(key, value)
        

    def get(self, key: int) -> int:
        bucket = key % 13337
        if self.hash_map[bucket] == None:
            return -1

        currPtr = self.hash_map[bucket]

        while currPtr != None:
            if currPtr.key == key:
                return currPtr.value

            currPtr = currPtr.next

        return -1


    def remove(self, key: int) -> None:
        
        bucket = key % 13337

        head = self.hash_map[bucket]

        if head == None:
            return

        currPtr = head

        if currPtr.key == key:
            self.hash_map[bucket] = currPtr.next
            return 
        
        while currPtr.next is not None:
            if currPtr.next.key == key:
                currPtr.next = currPtr.next.next
            
            currPtr = currPtr.next

        return


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1,2)
param_2 = obj.get(1)
print(param_2)
# obj.remove(key)