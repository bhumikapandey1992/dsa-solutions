# 121. Best Time to Buy and Sell Stock

## Problem in simple words

Choose one day to buy a stock and a later day to sell it. Return the largest possible profit, or `0` when every possible trade would lose money.

```text
prices = [7, 1, 5, 3, 6, 4]

Buy at 1 and sell later at 6.
Profit = 6 - 1 = 5
```

## Intuition

When considering a day as the selling day, the best buying price is the lowest price seen before or on that day. Track that minimum while scanning from left to right, then compare the current best profit with:

```text
today's price - lowest price seen so far
```

Scanning chronologically automatically guarantees that buying happens before selling.

## Step-by-step approach

1. Initialize `min_price` to infinity and `max_profit` to `0`.
2. For each price, update the lowest price seen so far.
3. Calculate the profit if the stock were sold at the current price.
4. Keep the largest profit found.
5. Return `max_profit`; it remains `0` when no profitable trade exists.

## Dry run

For `prices = [7, 1, 5, 3, 6, 4]`:

| Price | Minimum so far | Profit today | Maximum profit |
|---:|---:|---:|---:|
| 7 | 7 | 0 | 0 |
| 1 | 1 | 0 | 0 |
| 5 | 1 | 4 | 4 |
| 3 | 1 | 2 | 4 |
| 6 | 1 | 5 | 5 |
| 4 | 1 | 3 | 5 |

The answer is `5`.

## Implementation

```python
class Solution(object):
    def maxProfit(self, prices):
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit
```

## Complexity

- Time: `O(n)`
- Extra space: `O(1)`

## Edge cases

- A decreasing array returns `0`.
- One price returns `0` because no later selling day exists.
- The minimum price may occur after an earlier high price; only future selling prices are considered with it.

## Common mistake

Do not find the global minimum and maximum independently. The maximum price might occur before the minimum price, which would violate the required transaction order.

## What I learned

For a single buy-and-sell transaction, treat each day as a possible selling day and remember the cheapest valid buying price encountered so far.
