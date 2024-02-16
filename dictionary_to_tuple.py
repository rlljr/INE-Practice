# Dict to Tuple
# Create a function dict_to_tuple that receives a dictionary and returns a list of tuples containing the key-value pairs. Example:
#
# dict_to_tuple({'a': 1, 'b': 2})  # [('a', 1), ('b', 2)]
# dict_to_tuple({'Hello': 'World'})  # [('Hello', 'World')]

def dict_to_tuple(a_dict):
    tuple_list = [(k,v) for k,v in a_dict.items()]
    return tuple_list
    pass

print(dict_to_tuple({'a': 1, 'b': 2}))

