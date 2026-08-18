# Majority Element — Quick Revision

- **Pattern:** Frequency map with early return
- **Recognition clue:** Find the value occurring strictly more than half the time.
- **Count:** `count[num] = count.get(num, 0) + 1`
- **Threshold:** `len(nums) // 2`
- **Condition:** `count[num] > len(nums) // 2`
- **Why `>`:** Exactly half is not a majority.
- **Why early return:** Once a value exceeds half, no other value can also exceed half.
- **Time:** `O(n)`
- **Extra space:** `O(m)` for `m` distinct values
- **Common mistake:** Using `>=` and accepting a value that appears exactly half the time.
- **Memory sentence:** Count election ballots and return the first candidate with strictly more than half.
