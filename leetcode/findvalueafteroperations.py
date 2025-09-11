'''
https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
'''

def finalValueAfterOperations(self, operations: List[str]) -> int:
    temp_val = 0
    for i in operations:
        if i == 'X++' or i == '++X':
            temp_val += 1
        else:
            temp_val -= 1
    return temp_val