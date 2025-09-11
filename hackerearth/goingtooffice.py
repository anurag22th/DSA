'''
https://www.hackerearth.com/practice/basic-programming/operators/basics-of-operators/practice-problems/algorithm/going-to-office-e2ef3feb/
'''
s=int(input())
o=list(map(int,input().split()))
c=list(map(int,input().split()))
d=o[0]+(s-o[1])*o[2]
e=c[1]+(s/c[0])*c[2]+s*c[3]
if d<e:
    print("Online Taxi")
else:
    print("Classic Taxi")