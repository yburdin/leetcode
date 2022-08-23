class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """

        if self.size <= index or index < 0:
            return -1

        current_node = self.head
        for i in range(index):
            current_node = current_node.next

        return current_node.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        """
        self.head = Node(val, self.head)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val as the last element of the linked list.
        """
        if self.size == 0:
            self.addAtHead(val)

        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next

            current_node.next = Node(val)
            self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the indexth node in the linked list.
        If index equals the length of the linked list, the node will be appended to the end of the linked list.
        If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)

        elif index == self.size:
            self.addAtTail(val)

        elif index < self.size:
            current_node = self.head
            for i in range(index - 1):
                current_node = current_node.next

            next_node = current_node.next
            current_node.next = Node(val, next_node)
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if self.size > index >= 0:
            current_node = self.head
            if index == 0:
                self.head = current_node.next
            else:
                for i in range(index - 1):
                    current_node = current_node.next

                current_node.next = current_node.next.next

            self.size -= 1
