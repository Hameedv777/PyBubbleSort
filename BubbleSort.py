def bubbleSort(arr):
     n=len(arr)
     #Travel throgh all elemaents in the lis.
     for i in range(n):
         #Last i  elements are already in place , so we don't need to check them.
         for j in range(0,n-i-1):
             #Swap if the element foud is greate  than the next element
             if arr[j]>arr[j+1]:
                 arr[j],arr[j+1]=arr[j+1],arr[j]
#Example usage:
my_list=[64,34,25,22,11,90]
print("Original List:",my_list)
bubbleSort(my_list)
print("Sorted list",my_list)
                     
     
     