class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                colder_i, colder_t = stack.pop()
                res[colder_i] = i - colder_i
            stack.append((i, t))
        return res
