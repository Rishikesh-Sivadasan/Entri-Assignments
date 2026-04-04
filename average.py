# Calculating average marks


def calculate_average(marks01):

    
    average = 0
    total_marks =0
   
    for i in marks01:  # looping inside the marks01 list and fetching each element

        total_marks = total_marks + i  # combing all marks together
    
    average = total_marks/5  # averaging the marks

    return average   # returning the marks to main

