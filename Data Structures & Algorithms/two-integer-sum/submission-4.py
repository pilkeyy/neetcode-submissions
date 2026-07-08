class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i,n in enumerate(nums):
            target_sum = target - n
            if target_sum in visited:
                return [visited[target_sum],i]
            visited.update({n:i})
        