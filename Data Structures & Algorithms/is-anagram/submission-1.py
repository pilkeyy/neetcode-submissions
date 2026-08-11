
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        c1 = Counter()
        c2 = Counter()  
        for i in range(len(s)):
            c1[s[i]] +=1
            c2[t[i]] +=1 
        return c1 == c2