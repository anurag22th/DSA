'''
https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/palindrome-check-2/
Problem
You have been given a String S. You need to find and print whether this string is a palindrome or not. 
If yes, print "YES" (without quotes), else print "NO" (without quotes).

Input Format
The first and only line of input contains the String S. The String shall consist of lowercase English alphabets only.

Output Format
Print the required answer on a single line
'''
def palindrome(s):
    if s == s[::-1]:
        return 'YES'
    else:
        return 'NO'
    return 0
st = input()
print(palindrome(st))