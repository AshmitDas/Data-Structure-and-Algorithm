class Node:

    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:

    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.head is None:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0  or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        before = temp.prev
        after = temp.next
        before.next = temp.next
        after.prev = temp.prev
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp


    # def remove(self, index):     <-- ANOTHER WAY OF REMOVE METHOD FOR DOUBLY LL
    #     if index < 0 or index >= self.length:
    #         return None
    #     if index == 0:
    #         return self.pop_first()
    #     if index == self.length - 1:
    #         return self.pop()

    #     temp = self.get(index)
        
    #     temp.next.prev = temp.prev
    #     temp.prev.next = temp.next
    #     temp.next = None
    #     temp.prev = None

    #     self.length -= 1
    #     return temp

    def print_list(self) -> None:
        if self.length == 0:
            return None
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_doublyLL = DoublyLinkedList(7)

my_doublyLL.append(8)
my_doublyLL.append(9)
my_doublyLL.append(10)
my_doublyLL.append(11)

# my_doublyLL.pop_first()
# print(my_doublyLL.get(6))
# my_doublyLL.pop_first()
# my_doublyLL.pop_first()
# my_doublyLL.pop()
# my_doublyLL.pop()
# my_doublyLL.prepend(1)
my_doublyLL.insert(1,3)

# print(my_doublyLL.remove(1))

my_doublyLL.print_list()




