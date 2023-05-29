
# 
        
    
#Selection Sort

# arr=[12,45,23,51,19,8]

def SelectionSort(arr,size):
    
    i=0  #arr[i]=12
    for i in range(i,len(arr)):  
        mid_val=i 
        for j in (i+1,len(arr)):   
            if arr[j]<arr[mid_val]:
                mid_value=j
        arr[i]=arr[mid_val]
        arr[mid_val]=arr[i]
    
arr=[12,45,23,51,19,8] 

SelectionSort(arr,len(arr))
print("Sorted Array",arr)                             

# arr=[12,45,23,51,19,8]

# for i in range(len(arr)):  
#         mid_val=i 
#         for j in range(i+1,len(arr)):   
#             if arr[j]<arr[mid_val]:
#                 mid_value=j
#         arr[i],arr[mid_val]=arr[mid_val],arr[i]     
# print(arr)



