class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        counter = Counter(nums)
        for item, count in counter.items():
            buckets[count].append(item)
        c = 0
        res = []
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

