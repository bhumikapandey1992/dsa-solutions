# 402. Remove K Digits

## Problem in simple words

Remove exactly `k` digits from `num` so the remaining number is as small as possible. The relative order of the remaining digits cannot change.

## Analogy: building the smallest price tag

Imagine building a price tag from left to right. A digit near the front matters much more than one near the end.

If the tag ends in `4` and the next digit is `3`, keeping `4` before `3` makes the price unnecessarily large. If a deletion remains, erase `4` so `3` can move forward.

The greedy rule is:

> When a smaller digit arrives, remove larger digits immediately before it while deletions remain.

The stack holds the digits we currently plan to keep.

## Important lines explained

### Start the stack

```python
stack = []
```

The stack stores the chosen digits in their original order. While deletions remain, the algorithm tries to keep it nondecreasing.

### Visit every digit

```python
for digit in num:
```

We scan left to right because we may delete digits, but we may not rearrange them.

### Central greedy decision

```python
while k > 0 and stack and stack[-1] > digit:
```

All three conditions matter:

- `k > 0`: a deletion is available.
- `stack`: a previous digit exists.
- `stack[-1] > digit`: the previous digit is larger than the new digit.

Removing that larger previous digit lets the smaller digit occupy a more significant position.

We use `while`, not `if`, because one small digit may remove several larger digits. If `1` arrives after `432`, it can pop `2`, `3`, and `4` if the budget permits.

### Remove the larger digit

```python
stack.pop()
k -= 1
```

`pop()` erases the larger digit. Since one removal was used, decrease `k` by one.

### Keep the current digit

```python
stack.append(digit)
```

After every useful pop—or after deletions run out—keep the current digit.

### Use leftover deletions

```python
if k > 0:
    stack = stack[:-k]
```

If deletions remain, the digits never decreased enough to trigger all the pops. The kept digits are nondecreasing, so the largest digits are at the end.

Example:

```text
12345, k = 2 -> 123
```

### Clean leading zeroes

```python
result = "".join(stack).lstrip("0")
```

Join the digits, then remove only zeroes at the front:

```text
0200 -> 200
```

Zeroes inside or at the end remain because they affect the number.

### Protect the empty-result case

```python
return result if result else "0"
```

If every digit was removed, or only leading zeroes remain, return the valid numeric string `"0"` instead of an empty string.

## Commented solution

```python
class Solution(object):
    def removeKdigits(self, num, k):
        stack = []

        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1

            stack.append(digit)

        if k > 0:
            stack = stack[:-k]

        result = "".join(stack).lstrip("0")

        return result if result else "0"
```

## Complete dry run

```python
num = "1432219"
k = 3
```

Start:

```text
stack = []
k = 3
```

### Read `1`

The stack is empty, so append:

```text
stack = [1]
k = 3
```

### Read `4`

`1 > 4` is false. Append `4`:

```text
stack = [1, 4]
k = 3
```

### Read `3`

`4 > 3` is true. Erase `4` so `3` moves forward:

```text
pop 4
stack = [1]
k = 2
```

Now `1 > 3` is false. Append `3`:

```text
stack = [1, 3]
k = 2
```

### Read the first `2`

`3 > 2` is true:

```text
pop 3
stack = [1]
k = 1
```

Now `1 > 2` is false. Append `2`:

```text
stack = [1, 2]
k = 1
```

### Read the second `2`

`2 > 2` is false because equal digits do not improve one another. Append:

```text
stack = [1, 2, 2]
k = 1
```

### Read `1`

`2 > 1` is true. Use the final deletion:

```text
pop 2
stack = [1, 2]
k = 0
```

Another `2` is greater than `1`, but no deletion remains. Append `1`:

```text
stack = [1, 2, 1]
k = 0
```

### Read `9`

No deletions remain, so append:

```text
stack = [1, 2, 1, 9]
```

### Build the result

```text
join -> 1219
strip leading zeroes -> 1219
```

Final answer:

```text
1219
```

## Leading-zero dry run

```python
num = "10200"
k = 1
```

When `0` arrives, it pops `1`. The kept stack eventually becomes:

```text
[0, 2, 0, 0]
```

Then:

```text
join -> 0200
lstrip zeroes -> 200
```

The result is `"200"`.

## Why the greedy choice is correct

When two kept digits decrease from left to right, removing the earlier larger digit puts a smaller digit in a more significant place. No deletion farther right can compensate for keeping that larger prefix digit.

If no decreasing pair remains, the prefix is already as small as possible. Any leftover removals should therefore come from the end.

## Complexity

- Time: `O(n)`. Each digit is appended once and popped at most once.
- Space: `O(n)` for the stack.

## Memory rule

> Pop a larger digit when a smaller digit arrives. If removals remain after the scan, trim from the right.
