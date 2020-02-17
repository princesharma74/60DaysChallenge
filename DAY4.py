# https://www.hackerrank.com/challenges/dynamic-array/problem
N = input().split() # N[0] is the number of sequences in the sequence list, N[1] is the number of queries
x = []
lastAnswer = 0
seqList = [x for i in range(int(N[0]))]
def Query1xy(x, y):
    global lastAnswer
    temp = []
    pos = int((x^lastAnswer)%int(N[0]))
    temp = seqList[pos].copy()
    temp.append(y)
    seqList.pop(pos)
    seqList.insert(pos, temp)
def Query2xy(x, y):
    global lastAnswer
    pos = int((x^lastAnswer)%int(N[0]))
    index = int(y%len(seqList[pos]))
    lastAnswer = seqList[pos][index]
    print(lastAnswer)
for i in range(0, int(N[1])):
    M = input().split()
    if int(M[0]) == 1: 
        Query1xy(int(M[1]), int(M[2]))
    elif int(M[0]) == 2:
        Query2xy(int(M[1]), int(M[2]))

    
