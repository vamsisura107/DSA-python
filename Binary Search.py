arr = [10, 20, 30, 40, 50]
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2  
        if arr[mid] == key:
            print("Element found at index:", mid)
            return
        elif arr[mid] < key:
            low = mid + 1 
        else:
            high = mid - 1     
    print("Element not found")
n=int(input("enter the element to be searched:"))
binary_search(arr, n)
