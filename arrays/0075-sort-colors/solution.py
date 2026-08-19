class Solution(object):
    def sortColors(self, nums):
        counts = [0, 0, 0]

        for color in nums:
            counts[color] += 1

        red, white, blue = counts
        nums[:red] = [0] * red
        nums[red:red + white] = [1] * white
        nums[red + white:] = [2] * blue
