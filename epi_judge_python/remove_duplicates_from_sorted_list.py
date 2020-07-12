from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def remove_duplicates(L: ListNode) -> Optional[ListNode]:
    # TODO - you fill in here.
    open_spot = None
    i1, i2 = L, L.next
    while i2:
        if i2.data == i1.data:
            if not open_spot:
                open_spot = i2
        elif i1 != i2:
            if open_spot:
                open_spot.data = i2.data
                open_spot = open_spot.next
        i1, i2 = i2, i2.next

    valid_elements = 1
    current = L
    while current.data != open_spot.data:
        valid_elements += 1
        print(current.data)
        current = current.next

    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'remove_duplicates_from_sorted_list.py',
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
