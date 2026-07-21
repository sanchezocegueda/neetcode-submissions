from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    rev = []
    for i in range(len(arr)):
        rev.append(arr.pop())

    return rev

# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
