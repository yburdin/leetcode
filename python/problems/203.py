from typing import Optional
from classes import ListNode
import pytest


# 203. Remove Linked List Elements
def remove_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    new_head = ListNode()
    cur_node = new_head
    while head:
        if head.val != val:
            cur_node.next = ListNode(head.val)
            cur_node = cur_node.next

        head = head.next

    return new_head.next


@pytest.mark.parametrize('input_list, val, expected_list', [
    ([1, 2, 6, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5]),
    ([], 1, []),
    ([7, 7, 7, 7], 7, []),
])
def test_remove_elements(input_list, val, expected_list):
    input_linked_list = ListNode.from_list(input_list)
    expected_linked_list = ListNode.from_list(expected_list)
    result_list = remove_elements(input_linked_list, val)

    assert result_list == expected_linked_list
