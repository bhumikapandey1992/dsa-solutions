# Longest Consecutive Sequence — Quick Revision

- **Pattern:** Set + sequence-start detection
- **Recognition clue:** Find consecutive numeric chains in an unsorted array without sorting.
- **Set benefit:** Average `O(1)` membership checks and automatic duplicate removal.
- **Start condition:** `(num - 1) not in num_set`
- **Walk:** Repeatedly check whether `current_num + 1` exists.
- **Initial streak:** `1` because the starting number counts.
- **Why linear:** Only sequence starts trigger walks; middle values are skipped.
- **Time:** `O(n)` average
- **Extra space:** `O(n)`
- **Common mistake:** Walking forward from every number and rescanning the same sequence.
- **Memory sentence:** Find each train’s engine by checking for a missing predecessor, then count its cars forward.
