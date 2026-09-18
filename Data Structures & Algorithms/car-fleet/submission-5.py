class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = sorted(list(zip(position, speed)), reverse=True)
        stack = []
        for position, speed in ps:
            time = (target - position) / speed
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)
