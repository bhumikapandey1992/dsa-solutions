# `Counter` practice problems

Use this document as the checklist for the `collections.Counter` phase. Solve
each problem without looking at an existing solution. For every solution, state
what the Counter's keys and values represent and analyze the time and space
complexity.

## Fundamental problems

### 1. Valid Anagram

Write:

```python
def is_anagram(s: str, t: str) -> bool:
```

Return whether the strings contain exactly the same characters with exactly the
same frequencies. Characters are case-sensitive.

```python
is_anagram("anagram", "nagaram")  # True
is_anagram("rat", "car")          # False
is_anagram("aab", "abb")          # False
is_anagram("", "")                # True
```

Counter focus: construct and compare frequency maps.

### 2. First Unique Character

Write:

```python
def first_unique_char(s: str) -> int:
```

Return the index of the first character that occurs exactly once. Return `-1`
when no unique character exists.

```python
first_unique_char("leetcode")      # 0
first_unique_char("loveleetcode")  # 2
first_unique_char("aabb")          # -1
first_unique_char("")              # -1
```

Counter focus: count first, then scan the original sequence to preserve order.

### 3. Multiset Intersection

Write:

```python
def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
```

Return the values common to both lists, including duplicates. Output order does
not matter. Each value must occur the minimum number of times it appears in
either input.

```python
intersect([1, 2, 2, 1], [2, 2])        # [2, 2]
intersect([4, 9, 5], [9, 4, 9, 8, 4])  # [4, 9], in any order
intersect([1, 1, 1], [1, 1])           # [1, 1]
intersect([], [1, 2])                   # []
intersect([1, 2], [3, 4])               # []
```

Counter focus: multiset intersection with `&` and expansion with `.elements()`.

### 4. Common Characters Across Words

Write:

```python
def common_chars(words: list[str]) -> list[str]:
```

Return every character appearing in every word, including duplicates. Output
order does not matter. Return an empty list for empty input.

```python
common_chars(["bella", "label", "roller"])  # ["e", "l", "l"]
common_chars(["cool", "lock", "cook"])      # ["c", "o"]
common_chars(["abc", "def"])                # []
common_chars(["aabb"])                       # ["a", "a", "b", "b"]
common_chars([])                              # []
```

Counter focus: repeatedly intersect several frequency maps.

### 5. Missing Inventory

Write:

```python
def missing_items(
    required: list[str], available: list[str]
) -> dict[str, int]:
```

Return each missing item and the additional quantity required. Do not include
items for which enough units are available.

```python
missing_items(
    ["apple", "apple", "banana"],
    ["apple"],
)
# {"apple": 1, "banana": 1}

missing_items(["pen", "book"], ["pen", "book", "book"])  # {}
missing_items(["a", "a", "a"], ["a"])                    # {"a": 2}
missing_items([], ["apple"])                              # {}
missing_items(["apple"], [])                              # {"apple": 1}
```

Counter focus: subtraction keeps only positive remaining counts.

## Additional Counter problems

### 6. Top K Frequent Elements

Write:

```python
def top_k_frequent(nums: list[int], k: int) -> list[int]:
```

Return the `k` most frequent values. Output order does not matter.

```python
top_k_frequent([1, 1, 1, 2, 2, 3], 2)  # [1, 2]
top_k_frequent([1], 1)                   # [1]
top_k_frequent([4, 4, 5, 5, 5, 6], 2)   # [5, 4]
```

Counter focus: `.most_common(k)`. Later, revisit this problem during the heap
phase and compare the approaches.

### 7. Ransom Note — LeetCode 383 (Easy)

Write:

```python
def can_construct(ransom_note: str, magazine: str) -> bool:
```

Return whether `ransom_note` can be constructed using the letters in `magazine`.
Each magazine character can be used at most once.

```python
can_construct("a", "b")      # False
can_construct("aa", "ab")   # False
can_construct("aa", "aab")  # True
can_construct("", "abc")    # True
```

Counter focus: determine whether any required character count is missing.

### 8. Find Words That Can Be Formed by Characters — LeetCode 1160 (Easy)

Write:

```python
def count_characters(words: list[str], chars: str) -> int:
```

A word is good when it can be formed using the characters in `chars`, with each
character used at most once per word. Return the sum of the lengths of all good
words.

```python
count_characters(["cat", "bt", "hat", "tree"], "atach")  # 6
count_characters(["hello", "world", "leetcode"], "welldonehoneyr")  # 10
count_characters([], "abc")  # 0
```

Counter focus: compare every word's requirements with one available-character
Counter.

### 9. Rearrange Characters to Make Target String — LeetCode 2287 (Easy)

Write:

```python
def rearrange_characters(s: str, target: str) -> int:
```

Return the maximum number of copies of `target` that can be formed from the
characters in `s`. Each character in `s` can be used at most once.

```python
rearrange_characters("ilovecodingonleetcode", "code")  # 2
rearrange_characters("abcba", "abc")                   # 1
rearrange_characters("abbaccaddaeea", "aaaaa")         # 1
```

Counter focus: for each target character, divide the available count by the
count required for one copy, then take the minimum.

### 10. Intersection of Two Arrays II — LeetCode 350 (Easy)

This is the LeetCode version of Fundamental Problem 3. Reimplement it from
scratch under platform constraints rather than copying the earlier solution.

```python
def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
```

```python
intersect([1, 2, 2, 1], [2, 2])        # [2, 2]
intersect([4, 9, 5], [9, 4, 9, 8, 4])  # [4, 9], in any order
```

Counter focus: use the minimum frequency found in the two inputs.

## Review questions

1. When does a set lose information that a Counter preserves?
2. What does Counter subtraction do with zero and negative results?
3. What is the difference between `.elements()` and `.most_common()`?
4. Why must First Unique Character scan the original string after counting?
5. How can you check whether one Counter supplies another across Python versions?
6. When should Top K Frequent Elements use a heap instead of `.most_common()`?

