# Count Occurrences
# Write a function that receives a list as input and returns a dictionary that counts how many times the data in the list is repeated.
#
# count_occurrences(["a", "b", "c", "a", "a", "b"])
#
# # {"a" : 3, "b" : 2, "c": 1}

def count_occurrences(a_list):
    occurrence = {item: a_list.count(item) for item in a_list}

    return occurrence
    pass



