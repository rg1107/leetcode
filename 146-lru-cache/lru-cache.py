class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.capacity = capacity
        self.count = 0
        self.head.next = self.tail
        self.tail.prev = self.head
        self.mp = dict()
        
    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1
        node = self.mp[key]
        self._remove_links(node)
        self._add_to_front(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1:
            node = self.mp[key]
            node.val = value
            return

        if self.count >= self.capacity:
            self._remove_from_tail()

        self._add_node(key, value)

    def _remove_links(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
    
    def _add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        node.next.prev = node
        self.head.next = node
    
    def _remove_from_tail(self):
        node = self.tail.prev
        self.tail.prev = node.prev
        node.prev.next = self.tail
        node.next = None
        node.prev = None
        del self.mp[node.key]
    
    def _add_node(self, key, value):
        node = Node(key, value)
        self._add_to_front(node)
        self.count += 1
        self.mp[key] = node

                



    
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)