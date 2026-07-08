from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = defaultdict(list)
        for str in strs:
            freq = [0] * 26
            for char in str:
                freq[ord(char)-ord("a")] += 1
            ret[tuple(freq)].append(str)
        return list(ret.values())