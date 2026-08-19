# Best Time to Buy and Sell Stock — Quick Revision

- **Pattern:** One-pass running minimum
- **Recognition clue:** Maximize one future sell minus one earlier buy.
- **Core idea:** For every selling day, use the lowest buying price seen so far.
- **State:** `min_price` and `max_profit`
- **Key operation:** `max_profit = max(max_profit, price - min_price)`
- **Time:** `O(n)`
- **Extra space:** `O(1)`
- **Common mistake:** Choosing a selling price that occurs before the buying price.
- **Memory sentence:** Carry the cheapest past price forward and test the profit at every day.
