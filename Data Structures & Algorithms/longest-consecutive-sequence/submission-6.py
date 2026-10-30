class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ret = 0
        for num in s:
            c = 0
            if not num - 1 in s:
                c+=1
                while num + 1 in s:
                    c+=1
                    num += 1
                ret = max(ret,c)
        return ret            