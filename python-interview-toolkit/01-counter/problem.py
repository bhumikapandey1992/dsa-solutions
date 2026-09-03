"""Five fundamental practice problems for collections.Counter."""

from collections import Counter


def is_anagram(str1: str, str2: str) -> bool:
    """Return whether both strings contain identical character frequencies."""
    if len(str1) != len(str2):
        return False

    return Counter(str1) == Counter(str2)


def first_unique_char(s: str) -> int:
    """Return the index of the first character that appears exactly once."""
    counts = Counter(s)

    for index, char in enumerate(s):
        if counts[char] == 1:
            return index

    return -1


def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    """Return the multiset intersection of two integer lists."""
    count1 = Counter(nums1)
    count2 = Counter(nums2)
    common = count1 & count2

    return list(common.elements())


def common_chars(words: list[str]) -> list[str]:
    """Return characters shared by every word, including duplicates."""
    if not words:
        return []

    counts = Counter(words[0])

    for word in words[1:]:
        counts &= Counter(word)

    return list(counts.elements())


def missing_items(required: list[str], available: list[str]) -> dict[str, int]:
    """Return each unavailable item and the additional quantity needed."""
    count_req = Counter(required)
    count_ava = Counter(available)
    missing = count_req - count_ava

    return dict(missing)


def main() -> None:
    anagram_examples = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("aab", "abb", False),
        ("", "", True),
    ]

    for first, second, expected in anagram_examples:
        result = is_anagram(first, second)
        print(f"{first!r}, {second!r} -> {result}")
        assert result == expected

    assert first_unique_char("leetcode") == 0
    assert first_unique_char("loveleetcode") == 2
    assert first_unique_char("aabb") == -1
    assert first_unique_char("") == -1

    assert sorted(intersect([1, 2, 2, 1], [2, 2])) == [2, 2]
    assert sorted(intersect([4, 9, 5], [9, 4, 9, 8, 4])) == [4, 9]
    assert sorted(intersect([1, 1, 1], [1, 1])) == [1, 1]
    assert intersect([], [1, 2]) == []
    assert intersect([1, 2], [3, 4]) == []

    assert sorted(common_chars(["bella", "label", "roller"])) == ["e", "l", "l"]
    assert sorted(common_chars(["cool", "lock", "cook"])) == ["c", "o"]
    assert common_chars(["abc", "def"]) == []
    assert sorted(common_chars(["aabb"])) == ["a", "a", "b", "b"]
    assert common_chars([]) == []

    assert missing_items(
        ["apple", "apple", "banana"], ["apple"]
    ) == {"apple": 1, "banana": 1}
    assert missing_items(
        ["pen", "book"], ["pen", "book", "book"]
    ) == {}
    assert missing_items(["a", "a", "a"], ["a"]) == {"a": 2}
    assert missing_items([], ["apple"]) == {}
    assert missing_items(["apple"], []) == {"apple": 1}

    print("All examples passed.")


if __name__ == "__main__":
    main()

