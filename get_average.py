# Get Average
# Complete the function get_average so that it returns the average of all the numbers in list_of_numbers.
#
# You'll need to use a for loop to calculate the total value of all the numbers added together.
#
# Then divide the total by the amount of items in your list to get your average.
#
# Hint: You'll need a variable to keep track of the total. You need to figure out whether that variable belongs inside or outside the for loop.

def get_average(list_of_numbers):
    total = 0
    for l in list_of_numbers:
        total += l
    average = total / len(list_of_numbers)
    return average

    pass