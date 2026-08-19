# 42. Trapping Rain Water

## Problem in simple words

Each array value is the height of a vertical bar. After rain falls, determine how many units of water remain trapped between the bars.

Water requires a boundary on both sides. A single tall wall cannot trap water by itself.

## The formula for one position

For any position, find:

- the tallest wall on its left;
- the tallest wall on its right.

The shorter of those walls sets the water level because water spills over the shorter side:

```text
water above this position
= min(tallest left wall, tallest right wall) - current height
```

If the result is not positive, that position traps no water.

## Important correction to the mental model

Do not find one globally tallest wall and subtract every smaller bar from it. Every position needs a valid wall on both sides.

For example:

```text
height = [5, 2, 1, 2, 1, 4]
```

For a bar of height `1` between these boundaries:

```text
tallest left wall  = 5
tallest right wall = 4

water = min(5, 4) - 1
      = 4 - 1
      = 3
```

We use `4`, not the global maximum `5`, because water would spill over the shorter right wall.

## Why use two pointers?

Calculating the tallest wall on both sides separately for every position would repeat work. Instead, scan inward while maintaining:

```text
left_max  = tallest wall seen while moving from the left
right_max = tallest wall seen while moving from the right
```

At every step, process the side with the shorter current boundary.

## Why process the shorter side?

Suppose:

```text
height[left] <= height[right]
```

The right side already provides a boundary at least as tall as the current left bar. Therefore, the left side is the limiting side, and any water at `left` can be determined from `left_max`.

If instead:

```text
height[left] > height[right]
```

The left side already provides a boundary taller than the current right bar. The right side is limiting, so calculate using `right_max`.

### Memory rule

```text
Shorter side controls the water level.
Process that side, then move its pointer inward.
```

## Processing the left pointer

When `height[left] <= height[right]`:

```python
if height[left] >= left_max:
    left_max = height[left]
else:
    water += left_max - height[left]

left += 1
```

- A new taller bar updates `left_max`.
- A shorter bar traps the difference between `left_max` and its height.

For `height = [4, 2, 0, 3, 2, 5]`, the right endpoint `5` is at least as tall as every left bar encountered, so the left pointer handles all interior positions:

| Current height | `left_max` | Added water |
|---:|---:|---:|
| 4 | 4 | 0 |
| 2 | 4 | 2 |
| 0 | 4 | 4 |
| 3 | 4 | 1 |
| 2 | 4 | 2 |

Total water is `2 + 4 + 1 + 2 = 9`.

## Processing the right pointer

When `height[left] > height[right]`:

```python
if height[right] >= right_max:
    right_max = height[right]
else:
    water += right_max - height[right]

right -= 1
```

- A new taller bar updates `right_max`.
- A shorter bar traps the difference between `right_max` and its height.

For `height = [5, 2, 1, 2, 1, 4]`, the left endpoint `5` is taller than the right boundary `4`, so the right pointer resolves the interior positions:

| Current height | `right_max` | Added water |
|---:|---:|---:|
| 4 | 4 | 0 |
| 1 | 4 | 3 |
| 2 | 4 | 2 |
| 1 | 4 | 3 |
| 2 | 4 | 2 |

Total water is `3 + 2 + 3 + 2 = 10`.

## Both pointers can move

The pointer movement depends on the input:

- Sometimes several left positions are processed consecutively.
- Sometimes several right positions are processed consecutively.
- In many arrays, the algorithm alternates between them.

At each iteration, the comparison chooses the side whose answer is already safe to calculate.

## Implementation

```python
class Solution(object):
    def trap(self, height):
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        water = 0

        while left < right:
            if height[left] <= height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]

                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]

                right -= 1

        return water
```

## Complexity

- Time: `O(n)`
- Extra space: `O(1)`

## Edge cases

- Fewer than three bars cannot trap water.
- Strictly increasing or decreasing heights trap no water.
- Equal-height boundaries can trap water between them.
- Multiple separate valleys contribute to the total independently.

## Common mistakes

- Using only the globally tallest wall instead of requiring boundaries on both sides.
- Moving the taller side instead of the shorter limiting side.
- Adding negative water when the current bar establishes a new maximum.
- Forgetting to accumulate water from every valid position.

## What I learned

Track the tallest wall seen from each end, but calculate water from the currently shorter side. For each processed position, subtract its height from that side's maximum and add the result to the total.
