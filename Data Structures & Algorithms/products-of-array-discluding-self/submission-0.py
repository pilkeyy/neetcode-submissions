class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        prefix = [1] * len(nums) 
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        suffix = [1] * len(nums)
        for i in range(len(nums)-1,0,-1):
            suffix[i-1] = suffix[i] * nums[i]

        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]
        return res


        