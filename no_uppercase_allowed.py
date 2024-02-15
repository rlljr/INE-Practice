# Complete the function neutralize_uppercase so that it returns stringy the same as it was received if there are no capital letters in it or an empty string "" if there were. You need to use a while loop to go through each letter of the string one at a time to check for uppercase letters.
#
# Examples:
# # String has no uppercase letters so returns input string unchanged
# >>>  neutralize_uppercase("snitch") == "snitch"
# 'snitch'
#
# # String has uppercase letters so returns empty string
# >>>  neutralize_uppercase("eXpelliarMus")
# ''

def neutralize_uppercase(stringy):
    for l in stringy:
        if l.isupper():
            return ""
        else:
            continue
    return stringy
    pass

