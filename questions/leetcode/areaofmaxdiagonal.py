'''
https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/
'''

import math
def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag = 0
        for i in dimensions:
            diag = math.sqrt(i[0]**2+i[1]**2)
            if diag > max_diag:
                max_diag = diag
                area = (i[0]*i[1])
            elif diag == max_diag:
                temp_area = i[0]*i[1]
                area = max(area, temp_area)
        return area