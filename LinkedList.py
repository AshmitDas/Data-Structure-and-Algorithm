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
        """Big O: O(1)"""
        # Adds a value to the end of the list.
        
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
        """Big O: O(n)"""
        # Removes a value(node) from the end of the list.
        
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
        return temp.value

    def prepend(self, value):
        """Big O: O(1)"""
        # Adds a value at the begining of the list.
        
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head 
            self.head = new_node
        self.length += 1
        return True

    def insert(self, index, value):
        """Big O: O(n)"""
        # Adds a value at a particular index given while calling the method.
        
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def pop_first(self):
        """Big O: O(1)"""
        # Removes a value(node) from the begining of the list.
        
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        """Big O: O(n)"""
        # Returns a value from a particluar index given while calling the method
        
        if index < 0 or index >= self.length:
            return None
        temp = self.head 
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        """Big O: O(n)"""
        # Changes the value at a particular index given while calling the method
        
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def remove(self, index):
        """Big O: O(n)"""
        # Removes a value(more specifically node) at a particular index given while calling the method.
        
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        """Big O: O(n)"""
        # Reverse the whole list i.e the indexing of the list get reversed.
        
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after 
        

    def print_list(self) -> None:
        """Big O: O(n)"""
        # Prints out the whole list.
        
        if self.length == 0:
            return None
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    

alinkedlist = LinkedList(1)
alinkedlist.append(2)
alinkedlist.prepend(0)
alinkedlist.pop()
alinkedlist.pop_first()
alinkedlist.remove(0)

alinkedlist.print_list()

