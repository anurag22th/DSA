'''
https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/is-zoo-f6f309e7/
Problem
You are required to enter a word that consists of and that denote the number of Zs and Os respectively. 
The input word is considered similar to word zoo if 2 X x = y

Determine if the entered word is similar to word zoo.

For example, words such as zzoooo and zzzoooooo are similar to word zoo but not the words such as zzooo and zzzooooo.

Input format

First line: A word that starts with several Zs and continues by several Os.
Note: The maximum length of this word must be 
.
Output format

Print Yes if the input word can be considered as the string zoo otherwise, print No.
'''
def zoo(s):
    x = s.count('z')
    y = s.count('o')
    if x*2 == y:
        return 'Yes'
    else:
        return 'No'
    return 0
s = input()
print(zoo(s))