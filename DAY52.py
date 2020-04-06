#https://codeforces.com/problemset/problem/4/A
n = int(input())
p = 0
q = n
for i in range(1, n): 
    p = i
    q = n - i
    #print(p, q)
    if q%2==0 and p%2==0: 
        print('YES')
        break
    else: 
        pass
if q%2==0 and p%2==0: 
    pass
else: 
    print('NO')

