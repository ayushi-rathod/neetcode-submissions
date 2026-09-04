class ListNode:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.hmap = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key in self.hmap:
            node = self.hmap[key]
            self.removeNode(node)
            self.addNodeInFront(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            node = self.hmap[key]
            node.val = value
            self.removeNode(node)
            self.addNodeInFront(node)
  
        else:
            node = ListNode(key, value)
            self.hmap[key] = node
            self.addNodeInFront(node)
            
            if self.capacity < len(self.hmap):   
                node = self.tail.prev
                self.removeNode(node)
                del self.hmap[node.key] 
        

    def removeNode(self, curr: ListNode) -> None:
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
    
    def addNodeInFront(self, node) -> None:
        self.head.next.prev = node
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node