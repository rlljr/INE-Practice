#
# Identity Matrix
# An identity matrix is defined in the following way:
#
# image
#
# Basically, all the elements in the diagonal are ones (1s) and the rest are zeros (0s).
#
# An identity matrix has a size associated. For example, this is an identity matrix of size 3:
#
# 1 0 0
# 0 1 0
# 0 0 1
# And this is a matrix of size 5:
#
# 1 0 0 0 0
# 0 1 0 0 0
# 0 0 1 0 0
# 0 0 0 1 0
# 0 0 0 0 1
# A matrix is represented, Pythonically, with a "list of lists". Example:
#
# # size 3
# size_3_matrix = [
#     [1, 0, 0],
#     [0, 1, 0],
#     [0, 0, 1],
# ]
# # size 5
# size_5_matrix = [
#     [1, 0, 0, 0, 0],
#     [0, 1, 0, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 0, 1, 0],
#     [0, 0, 0, 0, 1],
# ]
# Write a function identity_matrix that receives a size parameter and builds an identity matrix using "lists of lists".


def identity_matrix(size):
    list_holder = []
    for y in range(size):
        sublist_holder =[]
        for x in range(size):
            if x == y:
                sublist_holder+="1"
            else:
                sublist_holder+="0"
        temp_holder = [int(a) for a in sublist_holder] # used for converting the 0,1s from text to integer
        list_holder.append(temp_holder)
    return list_holder
    pass


print(identity_matrix(5))