# Transform list to tuple
# Write a function list_2_tuple that takes a list as a parameter and returns a tuple containing the same elements. Example:

def list_2_tuple(a_list):
    my_new_tuple = tuple(a_list)
    print(my_new_tuple)
    return my_new_tuple

    # for a in a_list:
    #     my_new_tuple+=a
    # print (my_new_tuple)
    # return my_new_tuple
    pass

print(list_2_tuple([1,2,3,4,5,6]))