# Create counting list
# Define a function create_counting_list that receives a number to count up to. Normally because you know the number of loops you would want to use a for loop but in this case we will use a while loop to emulate a for loop.
#
# Return a list where each element counts up to the number provided starting from 1. If the number provided to count to is negative, return 'cannot be negative'.
#
# Examples:
#
# >>> create_counting_list(7)
# [1, 2, 3, 4, 5, 6, 7]
# >>> create_counting_list(3)
# [1, 2, 3]
# >>> create_counting_list(0)  # Special case, pay attention!
# []
# >>> create_counting_list(-1)  # Error if -1 is passed
# 'cannot be negative'
def create_counting_list(count_to_number):
    x = 1
    new_list = []
    if count_to_number == 0:
        return new_list
    if count_to_number < 0:
        return 'cannot be negative'
    while x <= count_to_number:
        new_list.append(x)
        x += 1
    return new_list

    pass

print(create_counting_list(-1))