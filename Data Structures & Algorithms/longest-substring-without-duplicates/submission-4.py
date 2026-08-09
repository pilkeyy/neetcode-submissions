class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l, r = 0, 0
        max_length = 0
        while r < len(s):
            if not s[r] in chars:
                chars.add(s[r])
            else:
                while s[r] in chars:
                    chars.remove(s[l])
                    l+=1
            chars.add(s[r])
            max_length = max(max_length, r - l + 1)
            r += 1
        return max_length
