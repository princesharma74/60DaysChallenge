#https://codeforces.com/problemset/problem/71/A
n = int(input())
a = []
for i in range(n): 
    a.append(input())
for i in a: 
    l = len(i)-2
    string = i[0]+str(l)+i[-1]
    if len(i)>10: 
        print(string)
    else: 
        print(i)
for _ in [0]*int(input()):
    s=input();l=len(s)-2;print([s,s[0]+str(l)+s[-1]][l>8])