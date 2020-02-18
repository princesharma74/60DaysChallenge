#https://www.hackerrank.com/challenges/array-left-rotation/problem
N = input().split()
input2 = input().split()
arr = [None for i in range(int(N[0]))]
get_arr = [None for i in range(int(N[0]))]
def leftRotate(arr1, d, n):
    global get_arr
    for i in range(n): 
        get_arr[(i+n-d)%n]=arr1[i] # d left rotation of n sized array = n-d right rotation of the array
for i in range(0, int(N[0])): # quick way to left rotate a number of times and assign the array simultaneosly 
    arr[i] = int(input2[i])
leftRotate(arr, int(N[1]), len(arr))
for i in range(0, len(arr)):
    print(get_arr[i], end=" ")
