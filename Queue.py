class Node:

    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Queue:

    def __init__(self, value) -> None:
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp
    

    def print_queue(self):
        if self.length == 0:
            return None
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

aqueue = Queue(3)

aqueue.enqueue(7)
aqueue.enqueue(9)

# print(aqueue.dequeue(), end='\n')
# print(aqueue.dequeue(), end='\n')
# print(aqueue.dequeue(), end='\n')
# print(aqueue.dequeue(), end='\n')

aqueue.print_queue()