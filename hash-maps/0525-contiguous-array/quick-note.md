# Contiguous Array — Quick Revision

- **Pattern:** Prefix balance + earliest-index hash map
- **Transformation:** `1 → +1`, `0 → -1`
- **Analogy:** A hiker moves up for `1` and down for `0`.
- **Core proof:** Same altitude twice means the middle journey has net change zero.
- **Meaning:** Net zero means equal numbers of zeros and ones.
- **Base checkpoint:** `{0: -1}`
- **Map:** `first_seen[count]` stores the earliest index for each count.
- **Length:** `current_index - first_seen[count]`
- **First occurrence:** Preserve it to maximize distance.
- **Time:** `O(n)`
- **Extra space:** `O(n)`
- **Memory sentence:** Return to the same altitude, and the ups and downs between visits cancel.
