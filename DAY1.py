#https://www.hackerrank.com/challenges/arrays-ds/problem

#DAY 1
n = input()
n = int(n)
arr = input().split()
for i in range(n-1, -1, -1):
    print(arr[i], end=" ")


