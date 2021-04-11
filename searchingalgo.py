#Linear search
def linearSearch(arr , search_element):
    for i in range(len(arr)):
        if(arr[i]==search_element):
            print("Element found at",i,"position");
            return
    print("Element not Found");
    
#Binary search
def binarySearch(arr, low, high, search_element):
    if(high >= low):
        mid = (high +low)//2
        if(arr[mid]==search_element):
            return mid
        elif(arr[mid]>search_element):
            return binarySearch(arr, low, mid-1,search_element)
        else:
            return binarySearch(arr,mid+1,high,search_element)
    else:
        return -1
       
    


arr = list(map(int,input("Enter the array\n").strip().split()));
search_element = int(input("Enter the element to be searched\n"));
'''linearSearch(arr,search_element);
while True:
    response =input("Want to search more ?\n press y for yes \n press n to quit\n");
    if response == "y":
        x = int(input("please enter the element to be searched\n"))
        linearSearch(arr,x);
    else:
        break;'''
result = binarySearch(arr,0,len(arr),search_element)
if(result != -1):
    print("element found at ",str(result),"position");
else:
    print("element not found");
while True:
    response =input("Want to search more ?\n press y for yes \n press n to quit\n");
    if response == "y":
        x = int(input("please enter the element to be searched\n"))
        r = binarySearch(arr,0,len(arr), x);
        if(r != -1):
            print("element found at ",str(r),"position");
        else:
            print("element not found");
    else:
        break;



        
        





    
