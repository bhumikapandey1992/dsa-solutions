"""Practice 5: calculate quantities missing from an inventory."""

from collections import Counter


def missing_items(required: list[str], available: list[str]) -> dict[str, int]:
    count_req = Counter(required)
    count_ava = Counter(available)
    missing = count_req - count_ava
    return dict(missing)


if __name__ == "__main__":
    assert missing_items(
        ["apple", "apple", "banana"], ["apple"]
    ) == {"apple": 1, "banana": 1}
    assert missing_items(["pen", "book"], ["pen", "book", "book"]) == {}
    assert missing_items(["a", "a", "a"], ["a"]) == {"a": 2}
    assert missing_items([], ["apple"]) == {}
    assert missing_items(["apple"], []) == {"apple": 1}
    print("All Missing Inventory examples passed.")
