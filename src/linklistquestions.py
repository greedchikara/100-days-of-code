# Q1 find the middle element of the linkedlist
# Q2 reversing linked list

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, node):
        current = self.head
        if not current:
            self.head = node
        while current.next:
            current = current.next
        current.next = node

    def findMiddleNode(self):
        fastPointer = self.head
        slowPointer = self.head
        while fastPointer != None and fastPointer.next != None:
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next
        return slowPointer.value

    def reverseLinkedList(self):
        prev = None
        current = self.head
        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        self.head = prev

    def printLinkList(self):
        current = self.head
        printList = ""
        while current:
            strlist = str(current.value) + "->"
            printList += strlist
            current = current.next
        print printList + "None"


e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
e5 = Node(5)
e6 = Node(6)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
ll.append(e5)
ll.append(e6)

# Test get_position
# Should print 3
print ll.findMiddleNode()
ll.printLinkList()
ll.reverseLinkedList()
ll.printLinkList()
