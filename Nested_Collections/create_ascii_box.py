# Create ASCII Box
# Write a function create_box that takes three inputs: height (rows), width (columns), and a character char and creates a height × width box using the character char.
#
# For this exercise, it's recommended to use a nested for-loop. There are other ways of solving it (which might be a good starting point), but try reaching the nested for-loop solution.
#
# >>> create_box(3, 4, '*')
# '****
#  ****
#  ****'
# >>> create_box(2, 2, '@')
# '@@
#  @@'
# IMPORTANT: You need to return your box, not just print it.


def create_box(height, width, char):
    holder =''
    for r in range(height):
        for c in range(width):
            holder  += char
        holder += "\n"

    return holder

    pass

print(create_box(5,10,':)'))

holder = ''
myrange = height + 1
if order == "ASC":
    for r in range(myrange):
        for a in range(myrange):
            if a == r:
                break
            holder += char
        holder += '\n'
    return holder.lstrip('\n')
elif order == "DESC":
    for r in range(myrange):
        for a in range(myrange):
            if a == r:
                break
            holder += char
        holder += '\n'
    return holder[::-1].lstrip('\n')
pass