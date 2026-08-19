from bisect import bisect_left, bisect_right


class Solution(object):
    def fullBloomFlowers(self, flowers, people):
        starts = []
        ends = []

        # Separate every interval into independent start and end timelines.
        for start, end in flowers:
            starts.append(start)
            ends.append(end)

        # Sorting lets us count relevant events with binary search.
        starts.sort()
        ends.sort()

        answer = []

        for person in people:
            # bisect_right counts flowers with start <= person.
            started = bisect_right(starts, person)

            # bisect_left counts flowers with end < person. A flower ending
            # exactly at this time is still blooming because ends are inclusive.
            ended = bisect_left(ends, person)

            # Active flowers are those that started minus those already ended.
            answer.append(started - ended)

        return answer
