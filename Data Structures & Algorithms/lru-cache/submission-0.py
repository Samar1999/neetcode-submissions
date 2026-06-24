class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.n = capacity
        self.cache = {}

        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert_node(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def delete_node(self, node):
        prev = node.prev
        nxt = node.next
        
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.delete_node(self.cache[key])
            self.insert_node(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete_node(self.cache[key])
        
        node = Node(key, value)
        self.cache[key] = node
        self.insert_node(self.cache[key])

        if len(self.cache) > self.n:
            del self.cache[self.tail.prev.key]
            self.delete_node(self.tail.prev)
            


