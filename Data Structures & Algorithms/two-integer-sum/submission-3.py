class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,n in enumerate(nums):
            target_sum = target - n
            if target_sum in seen:
                return [seen[target_sum],i]
            seen.update({n:i})
        