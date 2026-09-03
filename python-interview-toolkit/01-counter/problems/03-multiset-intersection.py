"""Practice 3: find the multiset intersection of two lists."""

from collections import Counter


def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    count1 = Counter(nums1)
    count2 = Counter(nums2)
    common = count1 & count2
    return list(common.elements())


if __name__ == "__main__":
    assert sorted(intersect([1, 2, 2, 1], [2, 2])) == [2, 2]
    assert sorted(intersect([4, 9, 5], [9, 4, 9, 8, 4])) == [4, 9]
    assert sorted(intersect([1, 1, 1], [1, 1])) == [1, 1]
    assert intersect([], [1, 2]) == []
    assert intersect([1, 2], [3, 4]) == []
    print("All Multiset Intersection examples passed.")
