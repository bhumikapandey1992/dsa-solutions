# Subarray Sum Equals K — Quick Revision

- **Pattern:** Prefix-sum frequency map
- **Equation:** `current_prefix - earlier_prefix = k`
- **Needed prefix:** `current_prefix - k`
- **Map:** Prefix sum → number of times seen
- **Base frequency:** `{0: 1}`
- **Count:** Add every occurrence of the needed prefix.
- **Order:** Count matches before recording the current prefix.
- **Why frequency:** Different earlier checkpoints create different subarrays.
- **Time:** `O(n)` average
- **Extra space:** `O(n)`
- **Memory sentence:** Current total minus target tells me which earlier total to count.
