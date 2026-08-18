# Reorganize String — Quick Revision

- **Pattern:** Greedy + max-heap with one-turn cooldown
- **Recognition clue:** Repeated items must be separated, and the most frequent item is the hardest to place.
- **Impossible condition:** `max_frequency > (len(s) + 1) // 2`
- **Heap:** Store `(-count, character)` because Python provides a min-heap.
- **Greedy choice:** Place the most frequent character that is currently available.
- **Cooldown:** Hold the character just used outside the heap for one iteration.
- **Safe reinsertion:** Reinsert the previously held character only after placing a different current character.
- **Count update:** With negative counts, `count += 1` means one copy was consumed.
- **Time:** `O(n log k)`
- **Extra space:** `O(k)`
- **Common mistake:** Reinserting the current character too early, allowing identical adjacent characters.
- **Memory sentence:** Seat the largest available group, keep it outside for one seat, then let it return.
