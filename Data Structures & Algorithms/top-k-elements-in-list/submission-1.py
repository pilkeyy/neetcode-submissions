class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter()
        for n in nums:
            cnt[n] += 1
        l = []
        for n,c in cnt.most_common(k):
             l.append(n)
        return l
      


        