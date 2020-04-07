n, k = map(int, input().split())
score = list(map(int, input().split()))
count = 0
for i in score: 
    if i>0 and i>=score[k-1]: 
        count = count + 1
print(count)
