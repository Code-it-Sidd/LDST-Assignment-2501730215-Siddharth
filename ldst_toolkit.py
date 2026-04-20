class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.data = [None] * self.capacity

    def append(self, item):
        if self.size == self.capacity:
            old_cap = self.capacity
            self._resize(2 * self.capacity)
            print(f"Resizing from {old_cap} to {self.capacity}")
        self.data[self.size] = item
        self.size += 1

    def pop(self):
        if self.size == 0: return None
        self.size -= 1
        item = self.data[self.size]
        self.data[self.size] = None
        return item

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def __str__(self):
        return str([self.data[i] for i in range(self.size)])

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def remove(self, value):
        curr = self.head
        prev = None
        while curr:
            if curr.data == value:
                if prev: prev.next = curr.next
                else: self.head = curr.next
                return
            prev = curr
            curr = curr.next

    def __str__(self):
        res, curr = [], self.head
        while curr:
            res.append(curr.data)
            curr = curr.next
        return str(res)

class DoublyLinkedList:
    def __init__(self):
        self.head = self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insert_at(self, index, data):
        new_node = Node(data)
        curr = self.head
        for _ in range(index):
            if curr: curr = curr.next
        if curr:
            new_node.next = curr
            new_node.prev = curr.prev
            if curr.prev: curr.prev.next = new_node
            else: self.head = new_node
            curr.prev = new_node

    def remove(self, value):
        curr = self.head
        while curr:
            if curr.data == value:
                if curr.prev: curr.prev.next = curr.next
                else: self.head = curr.next
                if curr.next: curr.next.prev = curr.prev
                else: self.tail = curr.prev
                return
            curr = curr.next

    def __str__(self):
        res, curr = [], self.head
        while curr:
            res.append(curr.data)
            curr = curr.next
        return str(res)

class Stack:
    def __init__(self):
        self.list = SinglyLinkedList()
    def push(self, data):
        node = Node(data)
        node.next = self.list.head
        self.list.head = node
    def pop(self):
        if not self.list.head: return None
        val = self.list.head.data
        self.list.head = self.list.head.next
        return val
    def peek(self):
        return self.list.head.data if self.list.head else None
    def is_empty(self):
        return self.list.head is None

class Queue:
    def __init__(self):
        self.list = SinglyLinkedList()
    def enqueue(self, data):
        self.list.append(data)
    def dequeue(self):
        if not self.list.head: return None
        val = self.list.head.data
        self.list.head = self.list.head.next
        return val
    def front(self):
        return self.list.head.data if self.list.head else None

def is_balanced(expr):
    s = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in expr:
        if char in pairs.values(): s.push(char)
        elif char in pairs.keys():
            if s.is_empty() or s.pop() != pairs[char]: return False
    return s.is_empty()

if __name__ == "__main__":
    print("--- Dynamic Array ---")
    da = DynamicArray()
    for i in range(10):
        da.append(i)
        print(da)
    print(f"Pop: {da.pop()}")
    print(f"Pop: {da.pop()}")
    print(f"Pop: {da.pop()}")
    print(f"After pops: {da}")

    print("\n--- Singly Linked List ---")
    sll = SinglyLinkedList()
    for x in [3, 2, 1, 4, 5]: sll.append(x)
    print(sll)
    sll.remove(2)
    print(sll)

    print("\n--- Doubly Linked List ---")
    dll = DoublyLinkedList()
    for x in [1, 2, 3, 4, 5]: dll.append(x)
    print(dll)
    dll.insert_at(3, 99)
    print(dll)
    dll.remove(2)
    print(dll)

    print("\n--- Stack ---")
    st = Stack()
    st.push(10); st.push(20)
    print(f"Peek: {st.peek()}")
    print(f"Pop: {st.pop()}")

    print("\n--- Queue ---")
    qu = Queue()
    qu.enqueue(1); qu.enqueue(2)
    print(f"Front: {qu.front()}")
    print(f"Dequeue: {qu.dequeue()}")

    print("\n--- Parentheses Checker ---")
    for ex in ["([])", "([)]", "(((", ""]:
        print(f"{ex if ex else ' '} -> {is_balanced(ex)}")