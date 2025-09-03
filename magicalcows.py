'''
https://open.kattis.com/problems/magicalcows


'''
c,n,m = map(int, input().split())
farms = []
visit = []
for i in range(n+m):
    if i < n:
        farms.append(int(input()))
    else:
        visit.append(int(input()))
#1st attempt = cow ko double karta fir half wala apply karta(func)
'''
def farmmake(lst,c):
    nlst = []
    for i in range(len(lst)):
        # double cows ko tabtak % karna hai jab tak <=c na ho jaye(d.p)
        if lst[i] > c:
            # 2 nahi jitne bar divide hua
            nlst.append((lst[i]//2))
            nlst.append((lst[i]//2))
        else:
            nlst.append(lst[i])
    return nlst
for i in visit_days:
    temp_farm = [x* 2**i for x in farms]
    # 0 count wale farm nahiu dekhti inspector
    print(len(farmmake(temp_farm, c)))
    farms = farmmake(temp_farm, c)'''
table = [[0 for _ in range(c+1)] for _ in range(51)]
for cow in farms:
    table[0][cow] += 1

for day in range(50):
    for i in range(1,c+1):
        if table[day][i] == 0:
            continue
        if i*2 <= c:
            table[day+1][i*2] += table[day][i]
        else:
            table[day+1][i] += 2*table[day][i]

for i in visit:
    print(sum(table[i]))