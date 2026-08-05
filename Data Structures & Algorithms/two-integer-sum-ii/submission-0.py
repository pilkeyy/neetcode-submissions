class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l , r = 0, len(numbers)-1
        while l < r:
            if(numbers[l] + numbers[r] == target):
                return [l+1,r+1]
            m = l + (r - l) // 2
            if (numbers[l] + numbers[m] == target):
                return [l+1,m+1]
            if (numbers[r] + numbers[m] == target):
                return [m+1,r+1]
            if (numbers[l] + numbers[r] > target):
                r-=1
            else:
                l+=1
        




        