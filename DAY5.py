N = input().split()
input2 = input().split()
arr = [None for i in range(int(N[0]))]
def leftRotate(arr1, d, n):
    for i in range(d): 
        leftRotatebyOne(arr1, n)
def leftRotatebyOne(arr2, n): 
        temp = arr2[0]
        for j in range(n-1):
            arr2[j] = arr2[j+1]
        arr2[n-1] = temp
for i in range(0, int(N[0])):
    arr[i] = int(input2[i])
leftRotate(arr, int(N[1]), len(arr))
for i in range(0, len(arr)):
    print(arr[i], end=" ")
