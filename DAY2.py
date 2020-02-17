import array
row, cols = (6, 6)
x = [[None for i in range(6)] for j in range(6)] # x[[]] this is array declaration but it had only one row
for i in range(0, 6):
    arr = input().split()
    for j in range(0, 6):
        x[i][j] = arr[j]
sum_array = []
for i in range(0, 4):
    for j in range(0, 4):
        sum = int(x[i][j]) + int(x[i][j+1]) + int(x[i][j+2]) + int(x[i+1][j+1]) + int(x[i+2][j]) + int(x[i+2][j+1]) + int(x[i+2][j+2])
        sum_array.append(sum)
# print('RESULTANT SUMS: '+ str(sum_array)) # Print can only concatenate (+) strings not integer
max = sum_array[0]
for i in range(1, len(sum_array)): 
    if sum_array[i] > max: 
        max = sum_array[i]
print(max)
'''
# Python 3 program to demonstrate working  
# of method 1 and method 2. 
  
rows, cols = (5, 5) 
  
# method 2a 
arr = [[0]*cols]*rows 
  
# lets change the first element of the  
# first row to 1 and print the array 
arr[0][0] = 1
  
for row in arr: 
    print(row) 
# outputs the following 
#[1, 0, 0, 0, 0] 
#[1, 0, 0, 0, 0] 
#[1, 0, 0, 0, 0] 
#[1, 0, 0, 0, 0] 
#[1, 0, 0, 0, 0] 
  
# method 2b 
arr = [[0 for i in range(cols)] for j in range(rows)] 
  
# again in this new array lets change 
# the first element of the first row  
# to 1 and print the array 
arr[0][0] = 1
for row in arr: 
    print(row) 
  
# outputs the following as expected 
#[1, 0, 0, 0, 0] 
#[0, 0, 0, 0, 0] 
#[0, 0, 0, 0, 0] 
#[0, 0, 0, 0, 0] 
#[0, 0, 0, 0, 0]

'''
