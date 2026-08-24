# Continuous Subarray Sum — Quick Revision

- **Pattern:** Prefix remainder + earliest-index hash map
- **Core proof:** Equal prefix remainders cancel when subtracted.
- **Highlighted rule:** Same remainder twice means the middle sum is divisible by `k`.
- **Map:** `remainder → first index`
- **Base checkpoint:** `{0: -1}` detects valid subarrays starting at index `0`.
- **Length:** `current_index - old_index >= 2`
- **First occurrence:** Keep it to maximize the possible distance.
- **Time:** `O(n)`
- **Extra space:** `O(min(n, k))`
- **Common mistake:** Remembering the trick without seeing `r - r = 0`.
- **Memory sentence:** Same clock position twice means full laps happened between visits.
