# First - Second - Third - Last
# The function insert_human receives a list, a position and an element to insert (similar to the insert method). The difference is that the position is specified in a "human" manner. Examples:
#

list_1 = ['a', 'b', 'c']

def insert_human(a_list, position, elem):
    if position == 'first':
        a_list.insert(0,elem)
    elif position == 'second':
        a_list.insert(1,elem)
    elif position == 'third':
        a_list.insert(2,elem)
    elif position == 'last':
        a_list.insert(3,elem)

    return a_list
    pass

#print(list_1)
print(insert_human(list_1,"first","S"))

# CODE BELOW WOULD NOT WORK BECAUSE IT RETURNS NONE. CANT RETURN A LIST WITH INSERT METHOD
# def insert_human(a_list, position, elem):
#
#     return a_list.insert(elem,position)
#     pass
#
# list_1 = ['a', 'b', 'c']
#
# print(insert_human(list_1,position = 2,"x"))