# Valid Anagram — Quick Revision

- **Pattern:** Fixed frequency array
- **Recognition clue:** Compare character frequencies in two lowercase strings.
- **Early check:** Different lengths mean `False` immediately.
- **State:** A 26-slot array stores `frequency in s - frequency in t`.
- **Letter index:** `ord(character) - ord("a")`
- **Update:** Add `1` for a character from `s`; subtract `1` for a character from `t`.
- **Answer:** `all(x == 0 for x in count)`
- **Why it works:** Matching frequencies cancel to zero in every letter slot.
- **Time:** `O(n)`
- **Extra space:** `O(1)` because the array size is always 26.
- **Common mistake:** Comparing only unique letters and ignoring how many times each appears.
- **Memory sentence:** Deposit letters from `s`, withdraw letters from `t`, and check whether every drawer balances to zero.
