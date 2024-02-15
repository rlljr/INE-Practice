# Is Char in String
# Use a for loops to complete the function char_in_string to check if char_to_look_for is in a_string.
#
# Do NOT use the in keyword to determine if it is in there.
#
# Return True if it is there and False if it is not.
#
# Examples:

# >>>  char_in_string("abcdef", "X")
# False

def char_in_string(a_string, char_to_look_for):
    for character in a_string:
        if char_to_look_for == character:
            return True
        elif char_to_look_for != character:
            continue
    return False

    pass

print(char_in_string('abcdefg','g'))