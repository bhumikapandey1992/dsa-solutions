# Trapping Rain Water — Quick Revision

- **Pattern:** Two pointers with running maximums
- **Recognition clue:** Water above bars depends on boundaries from both sides.
- **Formula:** `min(left_max, right_max) - current_height`
- **State:** `left`, `right`, `left_max`, `right_max`, and total `water`
- **Choose side:** Process the shorter current boundary.
- **Left side:** Update `left_max` or add `left_max - height[left]`.
- **Right side:** Update `right_max` or add `right_max - height[right]`.
- **Time:** `O(n)`
- **Extra space:** `O(1)`
- **Common mistake:** Comparing every bar only with the global tallest wall.
- **Memory sentence:** Two walls are required; the shorter side sets the water level.
