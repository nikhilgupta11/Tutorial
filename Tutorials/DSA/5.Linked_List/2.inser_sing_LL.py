# created a node
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

# created a linked list class in which we are defining the methods for head-tail, for print, and for insert a node


class SLinkedList:

    # defining a head and tail in this method
    def __init__(self):
        self.head = None
        self.tail = None

    # defining for print the LL
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # insert in Linked List
    # making a method which is taking two parameters value and location
    def insertSLL(self, value, location):
        # creating a node
        newNode = Node(value)

        # checking if LL is blank or not
        if self.head is None:
            # add the newNode refrance to head
            self.head = newNode

            # add Tail to the Node
            self.tail = newNode
        else:
            # if location is 0 then we have to insert the node at first position
            if location == 0:

                # adding the refrance of head(last node refrance) to newly created node
                newNode.next = self.head

                # adding the refrance of newly created node to head
                self.head = newNode

            # checking for the last location
            elif location == -1:

                # set the next of newly created node to null
                newNode.next = None

                # set new node refrence to this last node
                self.tail.next = newNode

                # create a lnk between newly created node and Tail
                self.tail = newNode

            # this condition will run for any given position in Linked list
            else:
                # store the head in a variable beacuse we have to start the terverse from head
                tempNode = self.head

                # this variable for while condition
                index = 0

                # this condition is using for terverse the LL from 0 to location-1
                # every time this will assign a new node and increase the value of index by one.
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode


singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(44, 6)
print([node.value for node in singlyLinkedList])
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(4, 1)
print([node.value for node in singlyLinkedList])
singlyLinkedList.insertSLL(5, 3)
print([node.value for node in singlyLinkedList])
