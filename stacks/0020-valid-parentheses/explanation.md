# 20. Valid Parentheses

## Problem in simple words

Determine whether every opening bracket in a string is closed by the correct bracket in the correct order.

Valid bracket pairs are:

```text
()
[]
{}
```

Examples:

```text
"()[]{}" → valid
"([{}])" → valid
"(]"     → invalid type
"([)]"   → invalid order
```

## Why a stack?

A closing bracket must match the most recently opened bracket that has not yet been closed.

This is last-in, first-out behavior:

```text
opening bracket added last → bracket that must close first
```

A stack provides exactly that behavior:

- `append()` pushes an opening bracket.
- `stack[-1]` reads the most recent opening bracket.
- `pop()` removes it after a successful match.

## Matching map

```python
matching = {
    ")": "(",
    "]": "[",
    "}": "{",
}
```

Each key is a closing bracket, and its value is the opening bracket it requires.

```text
current `)` expects `(`
current `]` expects `[`
current `}` expects `{`
```

This design also lets us recognize a closing bracket with:

```python
if char in matching:
```

## Processing each character

### Opening bracket

An opening bracket is not a key in `matching`, so push it:

```python
stack.append(char)
```

### Closing bracket

A closing bracket must pass two checks:

```python
if not stack or stack[-1] != matching[char]:
    return False
```

#### Check 1: `not stack`

If the stack is empty, there is no opening bracket available to match the closing bracket.

```text
s = ")"
```

This must immediately return `False`.

#### Check 2: `stack[-1] != matching[char]`

The most recent opening bracket must be the exact type expected by the current closing bracket.

```text
stack top = "["
current closing bracket = ")"
expected opening bracket = "("

"[" != "(" → invalid
```

The `or` short-circuits: when the stack is empty, Python does not evaluate `stack[-1]`, preventing an index error.

### Successful match

If both checks pass, remove the matching opening bracket:

```python
stack.pop()
```

## Complete dry run: `"([{}])"`

| Character | Action | Stack afterward |
|---|---|---|
| `(` | Push | `[(]` |
| `[` | Push | `[(, []` |
| `{` | Push | `[(, [, {]` |
| `}` | Match `{`, then pop | `[(, []` |
| `]` | Match `[`, then pop | `[(]` |
| `)` | Match `(`, then pop | `[]` |

The stack is empty, so the string is valid.

## Why order matters: `"([)]"`

```text
( → push → [(]
[ → push → [(, []
) → expects (, but the top is [
```

Although the string contains matching quantities of each bracket type, they are nested in the wrong order. Return `False` immediately.

## Why return `not stack`?

After processing every character, all opening brackets must have been matched and removed.

```python
return not stack
```

- Empty stack → `not stack` is `True`.
- Non-empty stack → `not stack` is `False`.

For example, `"(("` never encounters a wrong closing bracket, but two unmatched opening brackets remain. The final empty-stack check correctly returns `False`.

## Implementation

### Commented pop-or-dummy version

This version pops immediately when it sees a closing bracket. If the stack is empty, it uses `"#"` as a dummy value:

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # Map each closing bracket to its opening counterpart.
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                # Pop the top element when possible. If the stack is empty,
                # use a dummy character that cannot match an opening bracket.
                top_element = stack.pop() if stack else "#"

                # The most recent opening bracket must match this closer.
                if mapping[char] != top_element:
                    return False
            else:
                # Opening brackets wait on the stack for their matching closer.
                stack.append(char)

        # An empty stack means every opening bracket was matched.
        return len(stack) == 0
```

The key line is:

```python
top_element = stack.pop() if stack else "#"
```

- If the stack contains an opener, pop and compare it.
- If the stack is empty, use `"#"`, which cannot equal `(`, `[`, or `{`.
- The comparison then returns `False` naturally for an unmatched closer.

### Concise peek-then-pop version

The alternative checks the stack and its top before popping:

```python
if not stack or stack[-1] != matching[char]:
    return False

stack.pop()
```

Both versions implement the same stack logic in `O(n)` time. The repository keeps both for comparison.

## Complexity

- Time: `O(n)`
- Extra space: `O(n)` in the worst case

The worst-case stack occurs when the string contains only opening brackets.

## Edge cases

- A closing bracket appears before any opening bracket.
- Bracket types do not match.
- Correct types appear in the wrong nesting order.
- Opening brackets remain after the scan.
- A single pair is valid.

## Common mistakes

- Checking only the total number of each bracket type and ignoring order.
- Accessing `stack[-1]` before checking whether the stack is empty.
- Forgetting to pop after a successful match.
- Returning `True` without verifying that the stack is empty at the end.

## What I learned

When closing symbols must match the most recent unmatched opening symbols, use a stack and compare every closer with the stack's top.
