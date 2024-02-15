# Sum of numbers in list
# Define a function sum_of_numbers_in_list that receives a list of numbers a_list of an unknown length and calculates the sum of those numbers using a for loop. Do not use the sum function.
#
# Examples:
#
# >>> sum_of_numbers_in_list([])
# 0
# >>> sum_of_numbers_in_list([4])
# 4
# >>> sum_of_numbers_in_list([2, 3])
# 5
# >>> sum_of_numbers_in_list([2, 3, 4])
# 9

def sum_of_numbers_in_list(a_list):
    the_sum = 0
    for num in a_list:
        the_sum +=num
    return the_sum
    pass

print(sum_of_numbers_in_list([10,20,30,40,50]))
