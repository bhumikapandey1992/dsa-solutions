# Group Anagrams — Quick Revision

- **Pattern:** Hash map + canonical key
- **Recognition clue:** Group strings that are equivalent despite different character order.
- **Canonical key:** `"".join(sorted(word))`
- **Why it works:** Anagrams produce the same sorted string; non-anagrams do not.
- **Map shape:** `sorted_signature → list of original words`
- **Initialization:** Create an empty list the first time a key appears.
- **Answer:** `list(groups.values())`
- **Time:** `O(n × k log k)`
- **Extra space:** `O(n × k)`
- **Common mistake:** Using a set of letters as the key, which loses duplicate counts.
- **Memory sentence:** Alphabetize every word’s letters and put matching labels into the same bin.
