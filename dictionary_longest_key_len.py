
# Largest key
# Write a function that receives a dictionary with only String keys and returns the longest key in the dictionary. Example:
#
# longest_key({'hello': 'World', 'abc': 123})  # hello
# longest_key({})  # None


def longest_key(a_dict):
    if a_dict == {}:
        return None
    key_list =[k for k,v in a_dict.items()]
    return max(key_list,key=len)
    pass


print(longest_key({'hello': 'World', 'abc': 123}))




