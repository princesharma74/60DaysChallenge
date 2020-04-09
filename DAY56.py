#https://codeforces.com/problemset/problem/118/A
n = input()
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
count = 0
n=n.lower()
string = n
for i in string: 
    if i in vowels: 
        string = string[:count] + string[count+1:]
        count = count - 1
    else: 
        string = string[:count]+"."+string[count:]
        count = count + 1
    count=count+1
print(string)