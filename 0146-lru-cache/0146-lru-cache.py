class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        
        self.oldest = self.latest = Node(0, 0)  # for dummy
        self.oldest.next = self.latest
        self.latest.prev = self.oldest
    
    def _remove(self, node):
        prev_node, next_node = node.prev, node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _insert(self, node):
        prev_node, next_node = self.latest.prev, self.latest

        prev_node.next = next_node.prev = node
        node.next = next_node
        node.prev = prev_node

    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])

            return self.cache[key].value
        
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]

            self._remove(node)
            
            node.value = value
            self._insert(self.cache[key])

            return
        
        new_node = Node(key, value)
        self._insert(new_node)
        self.cache[key] = new_node

        if self.capacity < len(self.cache):
            lru = self.oldest.next

            self._remove(lru)
            del self.cache[lru.key]

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)