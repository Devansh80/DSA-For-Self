#Implimenting binary search algorithm using the - (Iterative Method)

def binarySearch_Iter(arr, x):
    left = 0
    right = len(arr)-1
    mid = 0

    while left <= right:
        mid = (right+left)//2
        #if x is greater,ignore left half
        if arr[mid] < x:
            left = mid+1
        #if x is smaller, ignore right half
        elif arr[mid] > x:
            right = mid-1
        #given value of x is presented at mid
        else:
            return mid
    #If the element was not presented in the array it will return -1
    return -1


if __name__ == "__main__":
    
    arr = [2,3,4,10,50]
    x = 4
    result = binarySearch_Iter(arr, x)

    if result != -1:
        print(f"Element is presented at index: {result}")
    else:
        print("Element is not presented in array")
