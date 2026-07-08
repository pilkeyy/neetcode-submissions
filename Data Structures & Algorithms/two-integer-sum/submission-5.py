class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i,n in enumerate(nums):
            target_n = target - n
            if target_n in visited:
                return [visited[target_n],i]
            visited.update({n:i})
        