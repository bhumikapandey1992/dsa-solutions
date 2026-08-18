from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        # 1. Count how many times each character appears
        frequencies = Counter(s)

        # 2. If one character occupies too many positions, separation is impossible
        if max(frequencies.values()) > (len(s) + 1) // 2:
            return ""

        # 3. Python has a min-heap, so use negative counts to simulate a max-heap
        max_heap = [(-count, character) for character, count in frequencies.items()]
        heapq.heapify(max_heap)

        result = []

        # 4. Hold back the previously used character for one turn
        previous_count = 0
        previous_character = ""

        while max_heap:
            # 5. Choose the most frequent character that is currently available
            count, character = heapq.heappop(max_heap)
            result.append(character)
            count += 1

            # 6. The previous character is now safe to use again
            if previous_count < 0:
                heapq.heappush(max_heap, (previous_count, previous_character))

            # 7. Hold the current character out of the heap until the next turn
            previous_count = count
            previous_character = character

        return "".join(result)
