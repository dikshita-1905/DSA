#BINARY SEARCH
numbers=[2,5,7,9,34]
find=9
l=0
r=len(numbers)-1
for number in numbers:
    mid=(l+r)//2
    if numbers[mid]==find:
        print("Found",mid)
        break
    elif numbers[mid]>=find:
        r=mid-1
    else:
        l=mid+1