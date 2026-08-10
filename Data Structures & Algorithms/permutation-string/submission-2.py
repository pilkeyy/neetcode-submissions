from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        n = len(s2)
        if k > n:
            return False
        c1 = [0] * 26
        c2 = [0] * 26
        for i in range(k):
            c1[ord(s1[i]) - ord("a")] += 1
            c2[ord(s2[i]) - ord("a")] += 1
        if c1 == c2:
            return True
        for i in range(k, n):
            c2[ord(s2[i]) - ord("a")] += 1  ## expand
            c2[ord(s2[i - k]) - ord("a")] -= 1  ## remove old element
            if c1 == c2:
                return True
        return False
