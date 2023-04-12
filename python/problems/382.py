from common import *


class LinkedListRandom:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        cur_value = None
        element_number = 1

        cur = self.head
        if cur:
            cur_value = cur.val

        while cur:
            cur = cur.next
            element_number += 1
            if cur and random.random() < 1 / element_number:
                cur_value = cur.val

        return cur_value
