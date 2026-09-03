"""Representative Counter problem: Valid Anagram (LeetCode 242)."""

from collections import Counter


def is_anagram(first: str, second: str) -> bool:
    """Return whether both strings contain identical character frequencies."""
    return Counter(first) == Counter(second)


def main() -> None:
    examples = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("aab", "abb", False),
        ("", "", True),
    ]

    for first, second, expected in examples:
        result = is_anagram(first, second)
        print(f"{first!r}, {second!r} -> {result}")
        assert result == expected

    print("All examples passed.")


if __name__ == "__main__":
    main()


# Complexity:
# - Time: O(n + m), because both strings are counted and compared.
# - Space: O(k), where k is the number of distinct characters.

