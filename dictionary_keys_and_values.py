# Write a function that inverts a dictionary's keys and values so that all values are now keys, and that all keys are now values.
#
# a_dict = {1: 'a', 2: 'b', 3:'c'}
#
# invert_dict(a_dict) # {'a': 1, 'b': 2, 'c': 3}


def invert_dict(existing):
    # if extising == {}:
    #     return existing
    res = dict((v,k) for k,v in existing.items())
    return res
    pass


print(invert_dict({
        1: 'a', 2: 'b',
        3: 'c', 4: 'd',
        5: 'e'}))