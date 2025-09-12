'''
https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
'''

def countNegatives(self, grid: List[List[int]]) -> int:
        ''' Brute Force
        count = 0
        for i in grid:
            for j in i:
                if j<0:
                    count += 1
        return count'''
        #  sorted in non-increasing order both row-wise and column-wise, => binary search
        def box(row):#main sirf dhund raha hoon ke -ve kaha se start hua phir len() se minus
            left = 0
            right = len(row)
            while left < right:
                mid = left + (right-left)//2
                if row[mid] < 0:
                    right = mid
                else:
                    left = mid + 1
            return len(row) - left
        c = 0
        for i in grid:
            print(box(i))
            c += box(i)
        return c