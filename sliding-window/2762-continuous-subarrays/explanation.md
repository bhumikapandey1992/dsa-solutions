# 2762. Continuous Subarrays

## Problem in simple words

Count contiguous subarrays in which the absolute difference between every pair of elements is at most `2`.

Checking every pair is unnecessary. A subarray satisfies that rule exactly when:

```text
maximum value - minimum value <= 2
```

If the two extremes differ by at most `2`, every value between them also satisfies the condition.

## Analogy: people allowed into an elevator

Imagine each number is a person's height category. An elevator group is allowed only when the tallest and shortest people differ by at most `2`.

As the right door admits a new person:

1. Update who is tallest and shortest.
2. If their difference is too large, move the left door forward until the group is valid.
3. Count every valid group ending with the newest person.

The challenge is finding the current tallest and shortest efficiently as people enter and leave.

## Solution 1: two monotonic deques

We keep two lines of candidate indices:

- `max_q` is decreasing by value. Its front is the current maximum.
- `min_q` is increasing by value. Its front is the current minimum.

We store indices, not just values, so we know when a candidate has moved outside the window.

## How the maximum deque works

```python
while max_q and nums[max_q[-1]] <= nums[right]:
    max_q.pop()
max_q.append(right)
```

If the new value is greater than or equal to a value at the back, that older value can never become the maximum before the new value leaves:

- the new value is at least as large;
- the new value is newer, so it remains in the window longer.

The older candidate is dominated and can be removed. The largest surviving value stays at the front.

## How the minimum deque works

```python
while min_q and nums[min_q[-1]] >= nums[right]:
    min_q.pop()
min_q.append(right)
```

This is the mirror image. An older value greater than or equal to the new value cannot become the minimum before the newer value leaves.

The smallest surviving value stays at the front.

## Shrinking an invalid window

```python
while nums[max_q[0]] - nums[min_q[0]] > 2:
    left += 1

    if max_q[0] < left:
        max_q.popleft()
    if min_q[0] < left:
        min_q.popleft()
```

The deque fronts reveal the current extremes in `O(1)` time.

When their difference exceeds `2`, move `left` forward. If a front index is now smaller than `left`, that element is no longer inside the window and must be removed.

Use `while` because moving `left` once may not be enough.

## Why add `right - left + 1`?

After shrinking, `[left ... right]` is valid. Every suffix ending at `right` is also valid because removing elements cannot increase the range beyond the current maximum and minimum.

The possible starting indices are:

```text
left, left + 1, ..., right
```

Their count is:

```text
right - left + 1
```

These are new subarrays because they all end at the current `right` index.

## Deque implementation

```python
from collections import deque


class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        max_q = deque()
        min_q = deque()
        left = 0
        total_subarrays = 0

        for right in range(len(nums)):
            while max_q and nums[max_q[-1]] <= nums[right]:
                max_q.pop()
            max_q.append(right)

            while min_q and nums[min_q[-1]] >= nums[right]:
                min_q.pop()
            min_q.append(right)

            while nums[max_q[0]] - nums[min_q[0]] > 2:
                left += 1
                if max_q[0] < left:
                    max_q.popleft()
                if min_q[0] < left:
                    min_q.popleft()

            total_subarrays += right - left + 1

        return total_subarrays
```

## Complete deque dry run

```python
nums = [5, 4, 2, 4]
```

The expected answer is `8`.

### `right = 0`, value `5`

Add index `0` to both deques:

```text
max_q = [0:5]
min_q = [0:5]
max - min = 0
```

The window `[5]` is valid:

```text
add 0 - 0 + 1 = 1
total = 1
```

### `right = 1`, value `4`

Maximum deque: `5 > 4`, so keep `5` before `4`:

```text
max_q = [0:5, 1:4]
```

Minimum deque: `5 >= 4`, so pop `5` and append `4`:

```text
min_q = [1:4]
```

The extremes differ by `5 - 4 = 1`, so the window is valid.

New subarrays ending here:

```text
[4]
[5, 4]
```

```text
add 2
total = 3
```

### `right = 2`, value `2`

Maximum deque keeps all decreasing candidates:

```text
max_q = [0:5, 1:4, 2:2]
```

Minimum deque removes `4` because the newer `2` is smaller:

```text
min_q = [2:2]
```

Now:

```text
maximum - minimum = 5 - 2 = 3
```

The window is invalid. Move `left` from `0` to `1`. Index `0` leaves, so remove it from `max_q`:

```text
left = 1
max_q = [1:4, 2:2]
min_q = [2:2]
```

The new difference is `4 - 2 = 2`, so stop shrinking.

New valid subarrays ending at index `2`:

```text
[2]
[4, 2]
```

```text
add 2
total = 5
```

### `right = 3`, value `4`

For `max_q`, the new `4` removes `2` and the older equal `4`, then enters as the newest maximum candidate:

```text
max_q = [3:4]
```

For `min_q`, `2 < 4`, so both remain:

```text
min_q = [2:2, 3:4]
```

The difference is `4 - 2 = 2`, so the window `[4, 2, 4]` is valid.

New subarrays ending here:

```text
[4]
[2, 4]
[4, 2, 4]
```

```text
add 3
total = 8
```

Final answer:

```text
8
```

## Solution 2: frequency map

The simpler version stores the frequency of every value in the current window:

```python
class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        counts = {}
        left = 0
        total_subarrays = 0

        for right in range(len(nums)):
            counts[nums[right]] = counts.get(nums[right], 0) + 1

            while max(counts) - min(counts) > 2:
                counts[nums[left]] -= 1
                if counts[nums[left]] == 0:
                    del counts[nums[left]]
                left += 1

            total_subarrays += right - left + 1

        return total_subarrays
```

`max(counts)` and `min(counts)` operate on dictionary keys, which are the distinct values currently inside the window.

Deleting a key when its count reaches zero is essential. Otherwise, an old value outside the window could incorrectly remain the reported minimum or maximum.

## Frequency-map dry run

For `nums = [5, 4, 2, 4]`:

| Right | Add | Counts before shrinking | Shrink action | Valid window | Added | Total |
|---:|---:|---|---|---|---:|---:|
| 0 | 5 | `{5: 1}` | None | `[5]` | 1 | 1 |
| 1 | 4 | `{5: 1, 4: 1}` | None | `[5,4]` | 2 | 3 |
| 2 | 2 | `{5: 1, 4: 1, 2: 1}` | Remove `5` | `[4,2]` | 2 | 5 |
| 3 | 4 | `{4: 2, 2: 1}` | None | `[4,2,4]` | 3 | 8 |

At index `2`, `5 - 2 = 3`, so remove the leftmost `5`. Its frequency reaches zero, so delete key `5`. The remaining extremes are `4` and `2`.

## Comparing the solutions

### Monotonic deques

- Directly exposes maximum and minimum in `O(1)`.
- Each index is added once and removed at most once.
- Generalizes well to other sliding-window range problems.
- Time: `O(n)`.
- Space: `O(n)` worst case.

### Frequency map

- Easier to understand and implement.
- `max(counts)` and `min(counts)` scan the distinct keys.
- In this exact integer problem, a previously valid window contains at most three distinct values because its range is at most `2`; adding one value temporarily creates at most four keys. Thus the scans are bounded by a small constant and the overall time is still `O(n)` here.
- The same frequency-map pattern with a larger allowed range can become slower, while the deque solution remains `O(n)`.
- Space is `O(1)` for this exact threshold, with at most a few active keys.

## Memory rule

> The decreasing deque remembers possible tallest people; the increasing deque remembers possible shortest people. Once the elevator group is valid, every suffix ending at the newest person is valid too.
