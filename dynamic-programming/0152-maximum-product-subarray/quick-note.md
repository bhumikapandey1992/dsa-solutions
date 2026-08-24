# Maximum Product Subarray — Quick Revision

- **Pattern:** Dynamic programming with running maximum and minimum
- **Recognition clue:** Products can flip sign when a negative number appears.
- **State:** Largest and smallest products ending at the current position.
- **Negative number:** Swap `current_max` and `current_min` before updating.
- **Transition:** Compare starting at `num` against extending the previous chain.
- **Zero:** Naturally resets both products to zero.
- **Answer:** Largest `current_max` seen anywhere.
- **Time:** `O(n)`
- **Extra space:** `O(1)`
- **Common mistake:** Tracking only the maximum and losing a negative valley.
- **Memory sentence:** Keep the peak and valley; a negative flips them.
