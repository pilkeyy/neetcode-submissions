class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(zip(position,speed),reverse=True)

        for p,s in cars:
            time = (target - p) / s
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack) 

        


"""
    p = [1,4] s = [3,2]
    4 6
    7 8
    10 10
    1 fleets

    p = [4,1,0,7] s = [2,2,1,1]
    
    3 fleets
    10 - 7 = 3/1 = 3
    10 - 4 = 6/2 = 3
    10 - 1 = 9/1 = 9

    [7,4,1,0]


    p = [1,2,3] s = [3,1,1]


"""