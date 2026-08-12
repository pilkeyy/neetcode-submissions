class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        for i, n in enumerate(nums):
            target_n = target - n
            if target_n in ht.keys():
                return [ht.get(target_n), i]
            ht.update({n: i})
        return []
