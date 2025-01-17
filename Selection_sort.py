def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        
        min_id = 1 
        for j in range(i+1, n):
            if arr[j] < arr[min_id]:
                
                min_id = j 
                
                arr[i] , arr[min_id] = arr[min_id] , arr[i]
            
            
def print_array(arr):
    for val in arr:
        print(val, end="")
    print()

if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    
    print("Original array: ", end="")
    print_array(arr)
    selection_sort(arr)
    print("Sorted array: ", end="")
    print_array(arr)
    
    
    