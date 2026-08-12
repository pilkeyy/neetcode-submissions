class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums)+1)]
        res = []
        count = defaultdict(int)
        for i in range(len(nums)):
            count[nums[i]] += 1
        for num in count:
            buckets[count[num]].append(num)
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
