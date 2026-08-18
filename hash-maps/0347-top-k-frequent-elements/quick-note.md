# Top K Frequent Elements — Quick Revision

- **Pattern:** Frequency map + sorting
- **Recognition clue:** Return the `k` values with the largest occurrence counts.
- **Count:** `count[num] = count.get(num, 0) + 1`
- **Pair shape:** `count.items()` produces `(number, frequency)`.
- **Sort key:** `key=lambda x: x[1]`
- **Direction:** `reverse=True` puts the largest frequencies first.
- **Extract:** Take `sorted_items[i][0]` for the first `k` entries.
- **Time:** `O(n + m log m)`, where `m` is the number of distinct values.
- **Extra space:** `O(m)`
- **Common mistake:** Returning `x[1]` (the count) instead of `x[0]` (the number).
- **Memory sentence:** Count the votes, sort the leaderboard by votes, and return the first `k` contestants.
