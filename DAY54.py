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