class Solution(object):
    def maxDivScore(self, nums, divisors):
        # Start below every possible score so the first divisor becomes the
        # initial champion, even when its score is zero.
        max_score = -1

        # Start with infinity so any real divisor wins an initial score tie.
        best_divisor = float("inf")

        for divisor in divisors:
            current_score = 0

            # Count how many values are perfectly divisible by this divisor.
            for num in nums:
                if num % divisor == 0:
                    current_score += 1

            # A strictly higher score creates a new champion.
            if current_score > max_score:
                max_score = current_score
                best_divisor = divisor

            # If the scores tie, the smaller divisor becomes the champion.
            elif current_score == max_score:
                if divisor < best_divisor:
                    best_divisor = divisor

        return best_divisor
