# Count Elements with 's'
# Complete the function count_elems_with_s so that it uses a for loop to go through each item in list_of_treasure.
#
# If the letter 's' is in the item, keep count of it.
#
# Return the final count of items that contain the letter 's'.


def count_elems_with_s(list_of_treasure):
    s_count = 0
    for a in list_of_treasure:
        if 's' in a:
            s_count+=1
    return s_count


    pass
