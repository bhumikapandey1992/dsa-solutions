"""Practice 4: find characters shared by every word."""

from collections import Counter


def common_chars(words: list[str]) -> list[str]:
    if not words:
        return []
    counts = Counter(words[0])
    for word in words[1:]:
        counts &= Counter(word)
    return list(counts.elements())


if __name__ == "__main__":
    assert sorted(common_chars(["bella", "label", "roller"])) == ["e", "l", "l"]
    assert sorted(common_chars(["cool", "lock", "cook"])) == ["c", "o"]
    assert common_chars(["abc", "def"]) == []
    assert sorted(common_chars(["aabb"])) == ["a", "a", "b", "b"]
    assert common_chars([]) == []
    print("All Common Characters examples passed.")
