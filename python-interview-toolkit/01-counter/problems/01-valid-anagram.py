"""Practice 1: determine whether two strings are anagrams."""

from collections import Counter


def is_anagram(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False
    return Counter(str1) == Counter(str2)


if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("aab", "abb") is False
    assert is_anagram("", "") is True
    print("All Valid Anagram examples passed.")
