def subtract_reversed(a_list):
    my_list = a_list[::-1]
    list_length= len(my_list)
    if a_list == []:
        return 0
    difference = a_list[-1]
    for i,x in enumerate(a_list):
        if i == list_length-1:
            #print(i)
            break
        else:
            difference-=x
    return (difference)
    pass

print(subtract_reversed([1,2,50,50,50]))