import collections

class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0, self.left)
        self.left.next = self.right
        self.map = {}

    def length(self):
        return len(self.map)

    def pushRight(self, val):
        node = ListNode(val, self.right.prev, self.right)
        self.right.prev.next = node
        self.right.prev = node
        self.map[val] = node

    def pop(self, val):
        if val in self.map:
            node = self.map[val]
            prev, next = node.prev, node.next
            prev.next, next.prev = next, prev
            del self.map[val]

    def popLeft(self):
        res = self.left.next.val
        self.pop(res)
        return res

class LFUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.lfuCount = 0
        self.valMap = {}  # Map key -> val
        self.countMap = collections.defaultdict(int)  # Map key -> count
        self.listMap = collections.defaultdict(LinkedList)  # Map count -> linked list of keys

    def counter(self, key):
        cnt = self.countMap[key]
        self.countMap[key] += 1
        self.listMap[cnt].pop(key)
        self.listMap[cnt + 1].pushRight(key)

        if cnt == self.lfuCount and self.listMap[cnt].length() == 0:
            self.lfuCount += 1

    def get(self, key):
        if key not in self.valMap:
            return -1
        self.counter(key)
        return self.valMap[key]

    def put(self, key, value):
        if self.cap == 0:
            return

        if key not in self.valMap and len(self.valMap) == self.cap:
            res = self.listMap[self.lfuCount].popLeft()
            del self.valMap[res]
            del self.countMap[res]

        if key in self.valMap:
            self.valMap[key] = value
        else:
            self.valMap[key] = value
            self.countMap[key] = 1
            self.listMap[1].pushRight(key)
            self.lfuCount = 1

        self.counter(key)

# Example usage:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
