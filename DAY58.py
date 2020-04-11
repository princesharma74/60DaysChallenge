#https://codeforces.com/problemset/problem/231/A
'''prob = int(input())
know = []
for i in range(prob): 
    know.append(list(map(int, input().split())))
count = 0
for input in know: 
    solved = 0
    for i in input: 
        if i: 
            solved = solved + 1
    if solved >= 2: 
        count = count + 1
print(count)
'''
print(sum(input().count('1')>1 for x in [0]*int(input())))