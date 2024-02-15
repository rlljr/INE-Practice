# Get Bookmark Index
# Complete the function get_bookmark_index so that it searches the parameter list_of_pages and returns the index of the word "bookmark".


def get_bookmark_index(list_of_pages):
    my_index = 0
    for x in list_of_pages:
        if "bookmark" == x:
            print(my_index)
            return my_index
        else:
            my_index+=1
    pass

my_list = [27, 35, 100, "bookmark", 111]

get_bookmark_index(my_list)