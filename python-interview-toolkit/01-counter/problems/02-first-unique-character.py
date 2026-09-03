"""Practice 2: find the index of the first unique character."""

from collections import Counter


def first_unique_char(s: str) -> int:
    counts = Counter(s)
    for index, char in enumerate(s):
        if counts[char] == 1:
            return index
    return -1


if __name__ == "__main__":
    assert first_unique_char("leetcode") == 0
    assert first_unique_char("loveleetcode") == 2
    assert first_unique_char("aabb") == -1
    assert first_unique_char("") == -1
    print("All First Unique Character examples passed.")
