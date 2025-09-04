'''https://open.kattis.com/problems/amultiplicationgame'''
'''import sys
def winner(n):
    p = 1
    vals = []
    # yeh list main max aur min multiplication ka ans hai
    while p < 4294967295:
        vals.append(p*9)
        vals.append(p*2)
        p += 1
    for i, x in enumerate(vals):
        if x >= n:
            break
        if i%2 == 0:
            print('Ollie wins.')
        else:
            print('Stan wins.')
    
#idhar loop ka length hi nahi diya tha
for ele in range(30):
    n = int(input())
    winner(n)
num_list = iter(sys.stdin.read().splitlines())
for num in num_list:
    winner(int(num))'''
    
import sys 
def winner(n):
    p = 1
    lst = []
    while p < 4294967295:
        lst.append(p*9)
        lst.append(p*2*9)
        p *= 18
    for i, j in enumerate(lst):
        if j >= n:
            if i%2 == 0:
                print('Stan wins.')
            else:
                print('Ollie wins.')
            #ek hi bar n se bada chahiye nahi break kiya toh chalte chalega
            break
num_list = iter(sys.stdin.read().splitlines())
for nums in num_list:
    winner(int(nums))