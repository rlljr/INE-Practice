import random


def random_matrix(m, n):
    list_holder = []
    for y in range(m):
        sublist_holder =[]
        for x in range(n):
            if x == y:
                random_number = random.randint(0,100)
                if random_number not in sublist_holder or random_number not in list_holder:
                    sublist_holder.append(random_number)
            else:
                random_number = random.randint(0,100)
                if random_number not in sublist_holder or random_number not in list_holder:
                    sublist_holder.append(random_number)

            #print(sublist_holder)
        temp_holder = [int(a) for a in sublist_holder] # used for converting the 0,1s from text to integer
        list_holder.append(temp_holder)
    return list_holder
    pass


print(random_matrix(4,5))