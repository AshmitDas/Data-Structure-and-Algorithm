class Node:

    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node







abst = BinarySearchTree()

abst.insert(2)
abst.insert(1)
abst.insert(5)
abst.insert(9)
abst.insert(28)


# print(abst.root.value)
# print(abst.root.left.value)
# print(abst.root.right.value)

# print(abst.contains(9))
# print(abst.contains(2))

print(abst.min_value_node(abst.root))

print(abst.min_value_node(abst.root.right))