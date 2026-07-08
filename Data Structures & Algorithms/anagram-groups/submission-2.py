class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            ret[sorted_s].append(s)
        return list(ret.values())