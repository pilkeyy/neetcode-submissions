from bisect import bisect_left, bisect_right


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            c_sum = numbers[l] + numbers[r]
            if c_sum == target:
                return [l + 1, r + 1]
            if c_sum > target:
                r = bisect_right(numbers, target - numbers[l], l, r) - 1
            else:
                l = bisect_left(numbers, target - numbers[r], l, r)