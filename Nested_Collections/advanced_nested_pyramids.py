# Advanced Nested Pyramids
# Extend your previous solution to include a third parameter "order" which can be either "ASC" or "DESC. Depending of the order provided, the pyramid will be displayed in ascending order ("ASC") or descending order ("DESC"). Examples:
#
# A pyramid with 5 levels ASC:
#
# advanced_nested_pyramid(5, '*', 'ASC')
# *
# **
# ****
# *****
# ******
# A pyramid with 5 levels DESC:
#
# advanced_nested_pyramid(5, '*', 'DESC')
# *****
# ****
# ***
# **
# *
# A pyramid with 3 levels ASC:
#
# advanced_nested_pyramid(3, '#', 'ASC')
# #
# ##
# ###
# A pyramid with 3 levels DESC:
#
# advanced_nested_pyramid(3, '@', 'DESC')
# @@@
# @@
# @

def advanced_nested_pyramid(height, char, order):
    holder =''
    myrange = height+1
    if order == "ASC":
        for r in range(myrange):
            for a in range(myrange):
                if a == r:
                    break
                holder += char
            holder += '\n'
        return holder.lstrip('\n')
    elif order =="DESC":
        for r in range(myrange):
            for a in range(myrange):
                if a == r:
                    break
                holder += char
            holder += '\n'
        return holder[::-1].lstrip('\n')
    pass

print(advanced_nested_pyramid(5,'X',"ASC"))



