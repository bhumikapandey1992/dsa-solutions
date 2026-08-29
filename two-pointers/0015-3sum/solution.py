class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []

        # nums[i] is the fixed first value for this outer-loop iteration.
        for i in range(len(nums)):
            # After sorting, a positive fixed value means every available value
            # to its right is also positive, so their sum cannot be zero.
            if nums[i] > 0:
                break

            # Do not repeat the same fixed value and recreate old triplets.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Search only after i, keeping all three indices different.
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[right] + nums[left]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip equal pointer values before moving to the next pair.
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return result
