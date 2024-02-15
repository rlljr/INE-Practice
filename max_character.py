# Write a function max_char that receives a string and returns the "maximum" character in it. Max is defined as a < b < ... < z ignoring uppercase chars (all strings provided will be lowercase). Important: If the string received is empty, the result should be an empty string. Example:
#
# max_char('azg')  # 'z'
# max_char('')  # ''

def max_char(a_string):
    new_list = []
    for i in a_string:
        new_list.append(i.casefold())
    if new_list == []:
        return ""
    else:
        return max(new_list)
    pass


print(max_char('janbfTahdag'))