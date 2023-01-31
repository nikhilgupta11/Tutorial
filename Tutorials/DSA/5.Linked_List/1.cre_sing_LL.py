class singleLL:
    def __init__(self):
        self.head = None
        self.tail = None


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


# creted a object of class
SingalyLL = singleLL()

# assign a value to nodes
node1 = Node(1)
node2 = Node(2)

# connect head with node1
SingalyLL.head = node1

# connect node1(head.next) with node2
SingalyLL.head.next = node2

# connect tail with node2
SingalyLL.tail = node2
