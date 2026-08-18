class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord("a")] += 1
            count[ord(t[i]) - ord("a")] -= 1

        return all(x == 0 for x in count)

        # temp="abcdefghijklmnopqrstuvwxyz"
        # for i in temp:
        #     if s.count(i)!=t.count(i):
        #         return False
        # return True
