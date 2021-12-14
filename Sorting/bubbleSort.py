def bubbleSort(arr):
    
    # Traverse through all array elements
    n = len(arr)
    #Note: range(n) also work but outer loop will repeat one time more than needed.
    for i in range(n-1):
        # Last i elements are already in place
        # swapped = False
        for j in range(0, n-i-1):
            '''traverse the array from 0 to n-i-1
            Swap if the element found is greater
            than the next element'''
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # swapped = True

        # if not swapped:
        #     break

# Driver code to test above
if __name__ == '__main__':
    
    arr = [64, 34, 25, 12, 22, 11, 90]
    # size =  int(input("Enter the size of Array: "))
    # arr = []
    # for i in range(size):
    #     val = int(input("Now enter the elements: "))
    #     arr.append(val)
    bubbleSort(arr)
    print(arr)