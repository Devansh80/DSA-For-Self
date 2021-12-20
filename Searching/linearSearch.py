#Linear Search function
def linearSearch(arr, n, k):
    #going through array sequencially
    for i in range(n):
        if arr[i] == k:
            return i
    return -1
    
    


if __name__ == "__main__":

    n = int(input("Enter size of the array: "))
    arr = []
    for i in range(n):
        values = int(input("Enter Values: "))
        arr.append(values)

    k = int(input("Enter the key value which you want to search: "))
    result = linearSearch(arr, n, k)
    if result == -1:
        print("Element not found")
    else:
        print(f"Element found at index: {i}")