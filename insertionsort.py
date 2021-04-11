def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
            print(arr)
            
        arr[j + 1] = key
        print(arr)
        
 
 
# Driver code 
arr = list(map(int,input().strip().split()))
insertionSort(arr)
print(arr)

    '''7,3,4,1,5,2

    i =1
    key = 3
    j = 0
    j+1 = 1

    7,7,4,1,5,2

    i=1
    key =3
    j=-1
    j+1 = 0

    3,7,4,1,5,2
    i=2
    key =4
    j =1
    j+1 = 2
  3,7,7,1,5,2
  i=2
  key =4
  j=0
  j+1 =1
  3,3,7,1,5,2
   i=2
  key =4
  j=-1
  j+1 =0'''
  

    
    
    

    
        
    
     
     
     
     
