import time
start_time = time.time()
nm_arr = input().split()
collected_array = [0]*(int(nm_arr[0])+1)
x = 0
max = 0
for i in range(0, int(nm_arr[1])):
    abk_arr = input().split()
    # manipulation(int(abk_arr[0]), int(abk_arr[1]), int(abk_arr[2]))
    collected_array[int(abk_arr[0])]+=int(abk_arr[2])
    if (int(abk_arr[1])+1)<=int(nm_arr[0]):
        collected_array[int(abk_arr[1])+1]-=int(abk_arr[2])
for i in range(0, int(nm_arr[0])):
               x=x+collected_array[i]
               if max < x:
                   max = x
print(max)
print("--- %s seconds ---" % (time.time() - start_time))
