class DoublyLlinkedList
    def __init__ (self):
        self.head = none
        self.tail = none

    def setHead(self,node):
        pass

    def setTail(self,node):
        pass

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else
            node.next.prev = nodeToInsert
        node.next = nodeToInsert
        

    def insertAtPosition(self, position, nodeToInsert):
        pass

    def removeNodesWithValue(self, value):
        pass

    def remove(self, node):
        if node == self.Head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.remove
        self.removeNodeLinks(node)

    def containsNodeWithValue(self, value):
        node = self.head
        while node is not none and node.value != value :
            node = node.next
        return node is not None

    def removeNodeLinks(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None
