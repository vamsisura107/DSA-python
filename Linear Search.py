arr = [10, 20, 30, 40, 50]
def linear_search(arr, key):
    for i in range(len(arr)): 
        if arr[i] == key:         
            print("Element found at index:", i)
            return                        
    print("Element not found")
n=int(input("eneter the element to be searched:"))
linear_search(arr, n)
