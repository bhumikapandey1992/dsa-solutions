# Valid Sudoku — Quick Revision

- **Pattern:** Sets + matrix traversal
- **Recognition clue:** Every filled cell must be unique across several overlapping regions.
- **Track:** Nine row sets, nine column sets, and nine box sets.
- **Ignore:** Skip `"."` cells.
- **Box index:** `(row // 3) * 3 + (column // 3)`
- **Box logic:** `(row // 3, column // 3)` first finds the two-coordinate box address.
- **Flattening:** Multiply the box row by `3` to skip bands, then add the box column.
- **Invalid condition:** The value already exists in its row, column, or box set.
- **Order:** Check first, then add the value to all three sets.
- **Time:** `O(1)` for the fixed 81-cell board; `O(n²)` if generalized.
- **Extra space:** `O(1)` for fixed Sudoku.
- **Common mistake:** Forgetting the 3×3 box check or treating `"."` as a digit.
- **Memory sentence:** Every digit passes three checkpoints: its row, its column, and its box.
