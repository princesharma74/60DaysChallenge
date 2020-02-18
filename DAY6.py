#https://www.hackerrank.com/challenges/sparse-arrays/problem
size_strings = int(input())
strings = [None for i in range(size_strings)]
for i in range(size_strings):
    strings[i] = input()
size_queries = int(input())
queries = [None for i in range(size_queries)]
for i in range(size_queries):
    queries[i] = input()
for i in range(size_queries):
    count=0
    for j in range(size_strings):
        if queries[i] == strings[j]:
            count+=1
    print(count)
