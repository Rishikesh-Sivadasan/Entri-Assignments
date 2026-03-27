
    # Armstrong numbers between a range

range_start = int(input("Enter the range start: "))
range_end = int(input("Enter the range end: "))


count =0

for i in range (range_start,range_end+ 1):

    value =0
    digits = len(str(i))
   
    data = str(i)
    
    for j in data:
        
        value += (int(j) ** digits)
       

    if value == i:
        print(f"{i} is a Armstrong number")
        count += 1

        
if count >0:
    print(f"There are {count} Armstrong numbers in between {range_start} and {range_end}") 

else:
    print(f"There are NO Armstrong numbers in between {range_start} and {range_end}") 
