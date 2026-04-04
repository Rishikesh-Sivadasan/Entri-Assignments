
# Calculating grade

def get_grade(average01):   

    # checking grades based on avaerage input from main

    if average01 >= 90:
        return "A"      # returning the grades based on the averages, all beow returns follow the same logic
    
    elif average01 >=80 and average01 <90:
        return "B"

    elif average01 >=70 and average01 <80:
        return "C"

    elif average01 >=60 and average01 <70:
        return "D"

    elif average01< 60:
        return "F"         
    
