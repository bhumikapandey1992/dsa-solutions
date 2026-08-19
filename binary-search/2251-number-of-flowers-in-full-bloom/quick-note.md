# Number of Flowers in Full Bloom — Quick Revision

- **Pattern:** Sorted event timelines + binary search
- **Condition:** A flower blooms when `start <= person <= end`.
- **Starts:** Sort every starting time.
- **Ends:** Sort every ending time.
- **Started count:** `bisect_right(starts, person)` gives `start <= person`.
- **Ended count:** `bisect_left(ends, person)` gives `end < person`.
- **Answer:** `started - ended`
- **Time:** `O(n log n + m log n)`
- **Extra space:** `O(n)`
- **Common mistake:** Removing a flower whose end equals the person's arrival time.
- **Memory sentence:** Right counts starts by now; left counts ends before now.
