def banana_dict(num):
    newdict = dict()
    for i in range(1, num + 1):
        newdict[i * "banaasdasdna"] = num
        newdict[i * "banaasdasdna"] = i
    return (newdict)

    pass


print(banana_dict(5))