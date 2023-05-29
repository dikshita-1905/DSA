#LINEAR SEARCH
numbers=[3,5,67,5,8]
find=5
i=0

for number in numbers:
    if number==find:
        found=True
        print("Found",i)
        
    else:
        i=i+1