# Get Search Match Indexes
# It's time to search our list_being_frisked for "suspicious" items. We want you to return the a new list containing the indexes of any items that match the string "suspicious".
#
# Hint: You'll need to keep track of the index and create a new list to store the indexes in.
#
# Good luck! You wanted to work for the TSA, right?


def get_search_match_indexes(list_being_frisked, search_term):
    new_list = []
    for count, value in enumerate(list_being_frisked):
        if search_term == value:
            new_list.append(count)
    print(new_list)
    return new_list

    pass


print(get_search_match_indexes(['aa','bb','cc','aa','bb','aa'],'aa'))