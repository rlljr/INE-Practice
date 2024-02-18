# Create Empty Box
# Expand on the last assigment and write a function create_empty_box that takes three inputs: height (rows), width (columns), and a character char and creates a height × width box using the character char that only has characters on the borders of the box (it's not filled in).
#
# If the box height or width are less than 3, return 'Invalid box dimensions' because it won't be an empty box.
#
# Hint: Look for patterns in the the way the empty box looks when you design your solution (top to bottom, side to side).
#
# >>> create_empty_box(3, 4, '*')
# '****
#  *  *
#  ****'
# >>> create_empty_box(5, 5, '@')
# '@@@@@
#  @   @
#  @   @
#  @   @
#  @@@@@'
# >>> create_empty_box(1, 1, '$')
# 'Invalid box dimensions'

# def create_empty_box(height, width, char):
#     holder = ''
#     max_row = height
#     min_row = 1
#     max_column = width
#     min_column = 1
#     for r in range(height):
#             if r == min_row or r == max_row:
#                 for c in range(width):
#                     if c == min_column or r == max_column:
#                         holder += char
#                     else:
#                         holder += " "
#                 holder += "\n"
#             else:
#                 holder+= " "
#
#     return holder
#
# pass
#
# print(create_empty_box(10,10,'X'))

def create_empty_box(height, width, char):
    holder =''
    for r in range(height):
        for a in range(width):
            if r == 0 or r == height-1 or a == 0 or a == width-1:
                holder+=char
            else:
                holder += " "
        holder += '\n'
    return holder.lstrip('\n')
    pass

print(create_empty_box(3,3,"X"))

