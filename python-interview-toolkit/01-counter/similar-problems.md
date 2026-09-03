# Counter practice problems

Solve these in order. Before coding, say what the Counter's keys and values will
represent. Afterward, record the time and space complexity in the explanation.

## Warm-up

1. Count every word in a sentence and return the most common word.
2. Given two lists, return their multiset intersection, including duplicates.
3. Decide whether the characters in one string can construct another string.

## Related LeetCode questions

| Order | # | Problem | Counter application |
|---:|---:|---|---|
| 1 | 242 | Valid Anagram | Compare character frequencies |
| 2 | 383 | Ransom Note | Check whether available counts cover needed counts |
| 3 | 349 | Intersection of Two Arrays | Compare keys; notice when a set is simpler |
| 4 | 350 | Intersection of Two Arrays II | Take the multiset intersection |
| 5 | 49 | Group Anagrams | Use a frequency signature as a grouping key |
| 6 | 451 | Sort Characters by Frequency | Order characters using their counts |
| 7 | 347 | Top K Frequent Elements | Combine frequency counting with sorting or a heap |

## Reflection questions

- When would a set lose information that a Counter preserves?
- How would you solve Valid Anagram without `Counter`?
- Why might `most_common(k)` be insufficient when a custom tie-breaker is given?
- For Top K Frequent Elements, when is a heap preferable to sorting everything?

