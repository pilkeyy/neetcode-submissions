class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c = defaultdict(int)
        l = 0
        mf = 0
        for r in range(len(s)):
            c[s[r]] +=1
            mf = max(mf,c[s[r]])
            while (r - l + 1) - mf > k:
                c[s[l]] -=1
                l+=1
        return r - l + 1