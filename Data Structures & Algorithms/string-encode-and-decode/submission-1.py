from functools import reduce


class Solution:
    def encode(self, strs: List[str]) -> str:
        return reduce(lambda acc, x: acc + str(len(x)) + "#" + x, strs, "")

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = s.find("#", i)

            length = int(s[i:j])

            i = j + 1

            res.append(s[i : i + length])

            i += length

        return res
