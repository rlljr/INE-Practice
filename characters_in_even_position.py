# Characters in even positions
# Write a function chars_in_even_positions that receives a string and returns all the characters in even positions. Example:
#
# chars_in_even_positions('Marvelous')  # avlu
# chars_in_even_positions('Python')  # yhn


def chars_in_even_positions(a_string):
    even_position = []
    for i in range(len(a_string)):
        if (i%2 == 0):
            even_position.append(a_string[i])
            new_string = "".join(str(e) for e in even_position)
            #print(new_string)
        else:
            continue
    return new_string

    pass



print(chars_in_even_positions('QWERTY12345'))
