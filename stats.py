"""
This module is a collection of statistical functions for analyzing
the results of a non-nominal survey question.

To test your current solution, run the `test_my_solution.py` file.
Refer to the instructions on Canavs for more information.

Author name: Shelby Kline
I have neither given nor received unauthorized assistance on
this assignment. I did not fabricate the answers to my
survey question.
"""
__version__ = 1

# 0) Question and Results
SURVEY_QUESTION = "How many dogs do you want to own?"
SURVEY_RESULTS = [2, 3, 69, 10, 2, 3, 2, 1, 2, 99, 2, 2, 3, 2, 3, 1, 3, 2, 2, 3, 3, 0]

# 1) count
"""
purpose: counts the number of items in SURVEY_RESULTS
uses the count pattern
"""
def count(SURVEY_RESULTS):
    count = 0
    for i in SURVEY_RESULTS:
        count = count + 1 
    return count
    
# 2) summate
"""
purpose: the combined total of the items in SURVEY_RESULTS
uses the summate pattern
"""
def summate(SURVEY_RESULTS):
    sum = 0 
    for i in SURVEY_RESULTS:
        sum = sum + i 
    return sum
    
        
# 3) mean
"""
purpose: to find the average of SURVEY_RESULTS 
uses sum divided by count
"""
def mean(SURVEY_RESULTS):
    if SURVEY_RESULTS == []:
        return None
    else:
        mean = summate(SURVEY_RESULTS) / count(SURVEY_RESULTS)
        return mean

# 4) maximum
"""
purpose: finds the largest number in SURVEY_RESULTS
sets max to a value that's smaller than any value
uses a for loop with an if statement
go through each number to test if it is the max"""
def maximum(SURVEY_RESULTS):
    maximum = -100000000
    if SURVEY_RESULTS == []:
        return None
    else:
        for i in SURVEY_RESULTS:
            if i > maximum:
                maximum = i 
    return maximum

# 5) minimum
"""
purpose: finds the smallest number in SURVEY_RESULTS
set minimum to a value that's larger than any value on the list
then use a for loop with an if statement
this will go through each number to test if it is the min"""  
def minimum(SURVEY_RESULTS):
    minimum = 1000000000
    if SURVEY_RESULTS == []:
        return None
    else:
        for i in SURVEY_RESULTS:
            if i < minimum:
                minimum = i
    return minimum

# 6) median
"""
purpose: to find the "middle" number 
sorts the list from smallest to largest and then finds the middle index
"""
def median(SURVEY_RESULTS):
    sorted_list = sorted(SURVEY_RESULTS)
    mid_index = int(count(SURVEY_RESULTS) / 2)
    if SURVEY_RESULTS == []:
        return None
    else:    
        return int(sorted_list[mid_index])

# 7) square
"""
purpose: to square all values in SURVEY_RESULTS
makes a new list for squared values
values are then set to the second power
"""
def square(SURVEY_RESULTS):
    square_list = []
    square_list = [i**2 for i in SURVEY_RESULTS]
    return square_list

# 8) standard_deviation
"""
purpose: to find the amount of variation in SURVEY_RESULTS
must have more than 2 items in SURVEY_RESULTS
"""
def standard_deviation(SURVEY_RESULTS):
    if count(SURVEY_RESULTS) < 2:
        return None
    else:
        sum_square = summate(square(SURVEY_RESULTS))
        sum = summate(SURVEY_RESULTS)
        values_cnt = count(SURVEY_RESULTS)
        stdev = ((sum_square - (sum * sum)/(values_cnt))/(values_cnt - 1))** .5
        stdev_rounded = round(stdev, 2)
        return stdev_rounded


# The following code can be used to try out your functions.
# Uncomment each line as you implement the functions to try them out.
# When you have implemented each function, copy the output from the
#   console into a comment below.
if __name__ == "__main__":
    print("We asked", count(SURVEY_RESULTS), "people the following question.")
    print('"'+SURVEY_QUESTION+'"')
    print("Here are the statistical results:")
    print("\tSum:", summate(SURVEY_RESULTS))
    print("\tMean:", mean(SURVEY_RESULTS))
    print("\tMedian:", median(SURVEY_RESULTS))
    print("\tMaximum:", maximum(SURVEY_RESULTS))
    print("\tMinimum:", minimum(SURVEY_RESULTS))
    print("\tSquare:", square(SURVEY_RESULTS))
    print("\tStandard Deviation:", standard_deviation(SURVEY_RESULTS))
    