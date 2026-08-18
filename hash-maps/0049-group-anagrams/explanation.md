# 49. Group Anagrams

## Problem in simple words

Given a list of words, place words containing exactly the same letters into the same group.

Anagrams use identical letters with identical frequencies, but the letters may appear in a different order.

```text
"eat", "tea", and "ate" are anagrams.
"tan" and "nat" are anagrams.
"bat" belongs to its own group.
```

For example:

```text
Input:  ["eat", "tea", "tan", "ate", "nat", "bat"]

Output:
[
  ["eat", "tea", "ate"],
  ["tan", "nat"],
  ["bat"]
]
```

The order of the groups and the words inside them does not matter.

## The key observation

Anagrams become identical when their letters are sorted.

```text
"eat" → "aet"
"tea" → "aet"
"ate" → "aet"

"tan" → "ant"
"nat" → "ant"

"bat" → "abt"
```

The sorted form acts as a shared signature, or dictionary key. Words with the same signature belong in the same list.

```text
sorted signature → original words

"aet" → ["eat", "tea", "ate"]
"ant" → ["tan", "nat"]
"abt" → ["bat"]
```

## Full analogy: a mail-sorting room

Imagine every word is a letter arriving at a mail room. The letters printed on the envelope may appear in any order, so the clerk needs a standard routing label.

The clerk performs three steps for every word:

1. Alphabetize its letters to create a routing label.
2. Find the bin carrying that label.
3. Place the original word—not the sorted label—inside the bin.

### The incoming conveyor belt

```text
┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐
│ eat │  │ tea │  │ tan │  │ ate │  │ nat │  │ bat │
└─────┘  └─────┘  └─────┘  └─────┘  └─────┘  └─────┘
```

### Create routing labels

```text
eat ──sort──→ aet
tea ──sort──→ aet
tan ──sort──→ ant
ate ──sort──→ aet
nat ──sort──→ ant
bat ──sort──→ abt
```

### Place each word in its matching bin

```text
┌───────────────────────────┐
│ Bin label: aet            │
│ Contents: eat, tea, ate   │
└───────────────────────────┘

┌───────────────────────────┐
│ Bin label: ant            │
│ Contents: tan, nat        │
└───────────────────────────┘

┌───────────────────────────┐
│ Bin label: abt            │
│ Contents: bat             │
└───────────────────────────┘
```

The dictionary `groups` is the entire wall of labeled bins:

```python
{
    "aet": ["eat", "tea", "ate"],
    "ant": ["tan", "nat"],
    "abt": ["bat"],
}
```

At the end, the routing labels are no longer needed. We return only the contents of the bins using `groups.values()`.

## Why sorting creates a reliable key

Two words are anagrams if and only if they contain the same characters with the same counts.

Sorting puts those characters into one canonical order:

```text
Different arrangements          One canonical arrangement

e a t ─┐
t e a ─┼── sort ──→ a e t
a t e ─┘
```

Repeated characters remain represented correctly:

```text
"aab" → "aab"
"aba" → "aab"
"abb" → "abb"   not the same key
```

Therefore:

- anagrams always produce the same key;
- non-anagrams always produce different keys.

## Complete dry run

Start with an empty dictionary:

```python
groups = {}
```

### Word 1: `"eat"`

```text
key = "aet"
```

The key does not exist, so create a list and append the word:

```python
groups = {
    "aet": ["eat"]
}
```

### Word 2: `"tea"`

```text
key = "aet"
```

The bin already exists:

```python
groups = {
    "aet": ["eat", "tea"]
}
```

### Word 3: `"tan"`

```text
key = "ant"
```

Create a new bin:

```python
groups = {
    "aet": ["eat", "tea"],
    "ant": ["tan"]
}
```

### Word 4: `"ate"`

```text
key = "aet"
```

```python
groups = {
    "aet": ["eat", "tea", "ate"],
    "ant": ["tan"]
}
```

### Word 5: `"nat"`

```text
key = "ant"
```

```python
groups = {
    "aet": ["eat", "tea", "ate"],
    "ant": ["tan", "nat"]
}
```

### Word 6: `"bat"`

```text
key = "abt"
```

```python
groups = {
    "aet": ["eat", "tea", "ate"],
    "ant": ["tan", "nat"],
    "abt": ["bat"]
}
```

Return the dictionary’s values:

```text
[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

## Implementation

```python
class Solution:
    def groupAnagrams(self, strs):
        groups = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())
```

## Line-by-line explanation

### Create the dictionary

```python
groups = {}
```

Each dictionary key will be a sorted signature. Its value will be the list of original words sharing that signature.

### Visit every word

```python
for word in strs:
```

Every input word must be assigned to exactly one group.

### Create the signature

```python
key = "".join(sorted(word))
```

`sorted(word)` returns a list of characters:

```text
sorted("tea") = ["a", "e", "t"]
```

`"".join(...)` combines them into a string that can be used as a dictionary key:

```text
"".join(["a", "e", "t"]) = "aet"
```

### Create a group when needed

```python
if key not in groups:
    groups[key] = []
```

The first word with a particular signature opens a new empty bin.

### Store the original word

```python
groups[key].append(word)
```

We append the original word because the output must preserve the words, not replace them with their sorted signatures.

### Return all groups

```python
return list(groups.values())
```

The keys helped organize the words, but the final answer needs only the grouped lists.

## Edge cases

### Empty string

The sorted signature of `""` is also `""`, so all empty strings are grouped together correctly:

```text
[""] → [[""]]
```

### One word

```text
["abc"] → [["abc"]]
```

### Duplicate words

Duplicates are kept as separate entries in the same group:

```text
["abc", "abc"] → [["abc", "abc"]]
```

### Same letters, different counts

```text
"aab" → "aab"
"ab"  → "ab"
```

They receive different keys and do not belong together.

## Complexity

Let:

- `n` be the number of words;
- `k` be the maximum length of a word.

Sorting one word costs `O(k log k)`, so:

- Time: `O(n × k log k)`
- Extra grouping space: `O(n × k)` for dictionary keys and stored words, excluding the returned output

## Common mistakes

- Using the original word as the key, which does not combine different arrangements.
- Using a set of characters as the key, which loses repeated-letter counts.
- Forgetting to join the sorted character list into a hashable string.
- Appending the sorted key instead of the original word.
- Returning the dictionary instead of its grouped values.
- Assuming output group order must match one specific example.

## What I learned

When equivalent objects can appear in many arrangements, transform each one into a canonical representation. That shared signature becomes a natural hash-map key.
