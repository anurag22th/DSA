'''
https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/find-product/

Problem
You have been given an array A of size N consisting of positive integers. 
You need to find and print the product of all the number in this array Modulo 10^9+7
.

Input Format:
The first line contains a single integer N denoting the size of the array. 
The next line contains N space separated integers denoting the elements of the array

Output Format:
Print a single integer denoting the product of all the elements of the array Modulo 10^9+7
'''
M = 1000000007
def prod(lst):
    ans = 1
    for i in lst:
        ans = (ans*i)%M
    return ans
N = int(input())
arr = list(map(int, input().split()))
print(prod(arr))