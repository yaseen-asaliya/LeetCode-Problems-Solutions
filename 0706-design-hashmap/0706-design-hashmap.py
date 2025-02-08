class ListNode:
    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.map = [ListNode() for _ in range(1000)]
    
    def hash(self, key: int) -> int: # index
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        cur = self.map[self.hash(key)] # at the top of dummy node (first element in linked list)
        while cur.next:
            if cur.next.key == key: # update
                cur.next.val = value 
                return
            cur = cur.next
        cur.next = ListNode(key, value) # insert 

    def get(self, key: int) -> int:
        cur = self.map[self.hash(key)].next # on dummy node next to avoid checking dumy value
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        cur = self.map[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)