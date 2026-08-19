# Two Sum II — Quick Revision

- **Pattern:** Two pointers from opposite ends
- **Recognition clue:** Find a target pair in a sorted array.
- **Start:** `left = 0`, `right = n - 1`
- **Too small:** Move `left` right to increase the sum.
- **Too large:** Move `right` left to decrease the sum.
- **Match:** Return `[left + 1, right + 1]` for 1-based positions.
- **Loop:** Continue while `left < right`.
- **Time:** `O(n)`
- **Extra space:** `O(1)`
- **Common mistake:** Returning zero-based indexes.
- **Memory sentence:** Too small moves left; too large moves right.
