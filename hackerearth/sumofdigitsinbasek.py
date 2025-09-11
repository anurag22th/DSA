'''
https://leetcode.com/problems/sum-of-digits-in-base-k/
'''

def sumBase(self, n: int, k: int) -> int:
    temp_num = n
    basek = ""
    sum_count = 0
    while temp_num:
        sum_count +=temp_num%k
        basek += str(temp_num%k)
        temp_num = temp_num//k
    basek = basek[::-1]
    num = int(basek)
    return sum_count
