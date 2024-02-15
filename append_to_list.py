# The append_to_list functions receives two parameters, hungry_list and data. Its job is to append the data passed to the hungry_list. Examples:
#
# a_list = ['pizza', 'bacon']
# modified_list = append_to_list(a_list, 'hamburger')
#
# print(modified_list)  # ['pizza', 'bacon', 'hamburger']

def append_to_list(hungry_list, data):
    hungry_list.append(data)
    return hungry_list
    pass

print(append_to_list([1,2,3], "hello"))
