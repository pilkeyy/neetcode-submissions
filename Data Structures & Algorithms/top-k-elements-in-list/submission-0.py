class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter()
        for n in nums:
            cnt[n] += 1
        list = []
        for n,c in cnt.most_common(k):
             list.append(n)
        return list
      


        