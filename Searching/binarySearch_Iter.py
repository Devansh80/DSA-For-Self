#Implimenting binary search algorithm using the - (Iterative Method)

def binarySearch_Iter(arr, x):
    left = 0
    right = len(arr)-1
    mid = 0

    while left <= right:
        mid = (right+left)//2
        #if x is greater,ignore left half
        if arr[mid] == x:
            return mid
        #if x is smaller, ignore right half
        elif arr[mid] < x:
            left = mid+1
        #given value of x is presented at mid
        else:
            right = mid-1
    #If the element was not presented in the array it will return -1
    return -1


if __name__ == "__main__":
    
    arr = [3, 4, 5, 6, 7, 8, 9]
    x = 5
    result = binarySearch_Iter(arr, x)

    if result != -1:
        print(f"Element is presented at index: {result}")
    else:
        print("Element is not presented in array")
