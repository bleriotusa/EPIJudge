import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:
    if len(A) == 1:
        return 1
    elif not A:
        return 0

    open_spot = -1
    i1, i2 = 0, 1
    while i2 < len(A):
        if A[i2] == A[i1]:
            if open_spot == -1:
                open_spot = i2
        elif A[i1] != A[i2]:
            if open_spot != -1:
                A[open_spot] = A[i2]
                open_spot += 1

        i1 += 1
        i2 += 1
    print(A)
    return open_spot if open_spot != -1 else len(A)


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
