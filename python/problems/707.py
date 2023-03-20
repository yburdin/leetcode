from common import *


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
        self.head = ListNode(val, self.head)
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

            current_node.next = ListNode(val)
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
            current_node.next = ListNode(val, next_node)
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


class TestMyLinkedList(unittest.TestCase):
    def test_707(self):
        with self.subTest(msg='Testcase 1'):
            my_linked_list = MyLinkedList()
            my_linked_list.addAtHead(1)
            my_linked_list.addAtTail(3)
            my_linked_list.addAtIndex(1, 2)                 # linked list becomes 1->2->3
            self.assertEqual(my_linked_list.get(1), 2)      # return 2

            my_linked_list.deleteAtIndex(1)                 # now the linked list is 1->3
            self.assertEqual(my_linked_list.get(1), 3)      # return 3

        with self.subTest(msg='Testcase 2'):
            my_linked_list = MyLinkedList()
            my_linked_list.addAtHead(7)
            my_linked_list.addAtHead(2)
            my_linked_list.addAtHead(1)
            my_linked_list.addAtIndex(3, 0)
            my_linked_list.deleteAtIndex(2)
            my_linked_list.addAtHead(6)
            my_linked_list.addAtTail(4)
            self.assertEqual(my_linked_list.get(4), 4)

            my_linked_list.addAtHead(4)
            my_linked_list.addAtIndex(5, 0)
            my_linked_list.addAtHead(6)

        with self.subTest(msg='Testcase 3'):
            my_linked_list = MyLinkedList()
            my_linked_list.addAtIndex(0, 10)
            my_linked_list.addAtIndex(0, 20)
            my_linked_list.addAtIndex(1, 30)
            self.assertEqual(my_linked_list.get(0), 20)

        with self.subTest(msg='Testcase 4'):
            my_linked_list = MyLinkedList()
            my_linked_list.addAtTail(1)
            self.assertEqual(my_linked_list.get(0), 1)

        with self.subTest(msg='Testcase 5'):
            my_linked_list = MyLinkedList()
            my_linked_list.addAtHead(4)
            self.assertEqual(my_linked_list.get(1), -1)
            my_linked_list.addAtHead(1)
            my_linked_list.addAtHead(5)
            my_linked_list.deleteAtIndex(3)
            my_linked_list.addAtHead(7)
            self.assertEqual(my_linked_list.get(3), 4)
            self.assertEqual(my_linked_list.get(3), 4)
            self.assertEqual(my_linked_list.get(3), 4)
            my_linked_list.addAtHead(1)
            my_linked_list.deleteAtIndex(4)


if __name__ == '__main__':
    unittest.main()
