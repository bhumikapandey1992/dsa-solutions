# Make Array Zero by Subtracting Equal Amounts — Quick Revision

- **Pattern:** Set / mathematical observation
- **Recognition clue:** The same amount is subtracted from every positive value in each operation.
- **Core observation:** Every operation removes exactly one distinct positive level.
- **Optimal choice:** Always subtract the current smallest positive value; choosing less eliminates nothing.
- **Why one level per operation:** Equal subtraction preserves the gap between different values, so larger distinct values remain positive.
- **Answer:** Number of distinct positive values in `nums`.
- **Implementation:** `return len(set(nums) - {0})`
- **Set difference:** `set(nums)` removes duplicates; `- {0}` removes zero.
- **Why duplicates do not matter:** Equal values receive identical subtractions and reach zero together.
- **Why zero does not matter:** It is already finished and is never changed.
- **Time:** `O(n)` average
- **Extra space:** `O(k)` for `k` distinct positive values
- **Common mistake:** Counting positive elements instead of distinct positive values.
- **Memory sentence:** Count the different building heights above ground; each height level needs one operation.
