# Get Positions of Char
# Use a for loop with enumerate to complete the function get_positions_of_char so that it looks at another_string and searches for characters that match char_being_searched_for. If it's a match, add the position to a result string followed by a comma. Example:
#
# get_positions_of_char("aabcda", "a") # Returns "0,1,5,"
# Hint: You might have to put str() around to position to change it from an integer into a string so you can add it to your result string.
#
# def get_positions_of_char(another_string, char_being_searched_for):
#
#     pass

def get_positions_of_char(another_string, char_being_searched_for):

    my_string =""
    for count, ele in enumerate(another_string):
        if ele == char_being_searched_for:
            my_string+=str(count)+","
    return my_string
    pass

# def chars_in_even_positions(a_string):
#     even_position = []
#     for i in range(len(a_string)):
#         if (i%2 == 0):
#             even_position.append(a_string[i])
#             new_string = "".join(str(e) for e in even_position)
#             #print(new_string)
#         else:
#             continue
#     return new_string
#
#     pass

print(get_positions_of_char("asdasdasd","x"))