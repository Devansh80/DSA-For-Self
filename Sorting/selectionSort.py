def selectionSort(arr):
    length = len(arr)
    for i in range(length-1):
        miniIndex = i
        for j in range(i+1, length):
            if arr[j] < arr[miniIndex]:
                miniIndex = j

            arr[i], arr[miniIndex] = arr[miniIndex],arr[i]

arr = [1,3,2,4,0,6,8]
selectionSort(arr)
print(arr)
        


    