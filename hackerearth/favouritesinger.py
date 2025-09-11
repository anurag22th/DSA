'''
https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/favourite-singer-a18e086a/

'''

from collections import Counter
def favourite_singer(arr):
    ans = 0
    counts = Counter(arr)
    max_count = max(counts.values())
    for i in counts.values():
        if i == max_count:
            ans += 1
    return ans
N = int(input())
lst = list(map(int, input().split()))
print(favourite_singer(lst))