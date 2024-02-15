

# Write a function insert_dashes that receives a string and inserts dashes every 3 characters. Example:
#
# insert_dashes('Hello World')  # 'Hel-lo -Wor-ld'
# insert_dashes('AwesomePythonRmotr')  # 'Awe-som-ePy-tho-nRm-otr-'
#
def insert_dashes(a_string):
    return '-'.join([a_string[i:i+3] for i in range(0, len(a_string)+1, 3)])
    pass

print(insert_dashes('asdasdasdasggdfgdfg'))

def insert_dashes(a_string):
    my_list=[]
    counter = 3
    for a in a_string:
        my_list.append(a)
        counter-=1
        if counter == 0:
            my_list.append('-')
            counter = 3
            continue
    new_string = "".join(str(e) for e in my_list)
    return (new_string)

print(insert_dashes('123456789dsdfsdfsdfsdf'))
