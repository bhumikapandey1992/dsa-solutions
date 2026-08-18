class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        sorted_items = sorted(
            count.items(),
            key=lambda x: x[1],
            reverse=True,
        )
        result = []

        for i in range(k):
            result.append(sorted_items[i][0])

        return result
