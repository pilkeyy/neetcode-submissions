class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix) , len(matrix[0])
        l, r = 0, row * col - 1

        while l <= r:
            m = (l + r) // 2
            rows , cols = m // col, m % col
            if matrix[rows][cols] == target:
                return True
            elif matrix[rows][cols] < target:
                l = m + 1
            else:
                r = m - 1
        return False

