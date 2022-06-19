from pickle import NONE


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None



class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1

        return True


    def pop(self):
        if self.length == 0:
            return None
        pre = self.head
        temp = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def print_list(self) -> None:
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next

    

alinkedlist = LinkedList(3)

alinkedlist.append(1)

print(alinkedlist.pop())
print(alinkedlist.pop())
print(alinkedlist.pop())