# Find the Maximum Divisibility Score — Quick Revision

- **Pattern:** Nested counting with a tie-breaker
- **Analogy:** Divisor teachers compete to divide the most test numbers.
- **Score condition:** `num % divisor == 0`
- **Reset:** Set `current_score = 0` for every divisor.
- **Higher score:** Update both `max_score` and `best_divisor`.
- **Tied score:** Keep the smaller divisor.
- **Initialization:** `max_score = -1`, `best_divisor = infinity`
- **Time:** `O(D × N)`
- **Extra space:** `O(1)`
- **Common mistake:** Forgetting the smallest-divisor tie-breaker.
- **Memory sentence:** Most points wins; smallest number wins a tie.
