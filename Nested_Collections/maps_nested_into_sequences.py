products = [{
    'id': 'W-101',
    'name': 'Arakh of Khal Drogo',
    'price': 250,
    'category': 'Weapons'
}, {
    'id': 'W-90',
    'name': 'Damascus Steel Widows Wail',
    'price': 960,
    'category': 'Weapons'
}, {
    'id': 'W-32',
    'name': 'Damascus Oathkeeper Sword',
    'price': 810,
    'category': 'Weapons'
}, {
    'id': 'S-81',
    'name': 'Lannister Shield',
    'price': 310,
    'category': 'Shields'
}, {
    'id': 'S-13',
    'name': 'Stark Infantry Shield',
    'price': 180,
    'category': 'Shields'
}, {
    'id': 'H-78',
    'name': 'Helm of the Unsullied',
    'price': 90,
    'category': 'Helms'
}, {
    'id': 'H-54',
    'name': "The Hound's Helm",
    'price': 120,
    'category': 'Helms'
}, {
    'id': 'H-67',
    'name': 'Helmet of Loras Tyrell',
    'price': 1378,
    'category': 'Helms'
}]

#Tasks:
#1. find most expensive item:

most_expensive_product = {}
for product in products:
    price = product['price']
    if price >= most_expensive_product.get('price',0):#needed or otherwise you get exception
        most_expensive_product = product
print(most_expensive_product)



#to look at this in the bigger picture. A single product is represented as a single dictionary
# P1 = {
#     'id': 'H-67',
#     'name': 'Helmet of Loras Tyrell',
#     'price': 1378,
#     'category': 'Helms'
# }
# P2 = {
#     'id': 'H-54',
#     'name': "The Hound's Helm",
#     'price': 120,
#     'category': 'Helms'
# }
#
# P3 = {
#     'id': 'H-78',
#     'name': 'Helm of the Unsullied',
#     'price': 90,
#     'category': 'Helms'
# }
#
# products = [P1,P2,P3]
#
# print(P1['price'])


#2. find most expensive weapon

most_expensive_product = {}
for product in products:
    price = product['price']
    cat = product['category']
    if price >= most_expensive_product.get('price',0) and cat == 'Weapons' :#needed or otherwise you get exception
        most_expensive_product = product
print(most_expensive_product)


#3. FInd the most expensive item per category. We're searcing for multiple items
weapons = []
most_expensive_weapon ={}
most_expensive_product = {}
for product in products:
    cat = product['category']
    if cat == 'Weapons':
        weapons.append(product)

for w in weapons:
    price = product['price']
    weapon_name = product['name']
    if price >= most_expensive_product.get('price',0) :#needed or otherwise you get exception
        most_expensive_weapon = weapon_name

print(most_expensive_weapon)

#4. calculate the total sum of prices of products
total_sum = 0
for product in products:
    total_sum+= product['price']
print(total_sum)

#5. Count the number of items per category
# Weapons: 3
# shields: 2
# Helms: 5
result = {} #we'll build this dictionary as we find products
#solution 1
for product in products:
    cat = product['category']
    result.setdefault(cat,0)
    result[cat] = result.get(cat, 0) + 1

#solution 2
# for product in products:
#     cat = product['category']
#     result.setdefault(cat,0)
#     result[cat]+=1

    # if cat not in result:
    # if cat not in result:
    #     result[cat] = 0
    # else:
    #     result[cat] += 1
print(result)

print('X'*2000)


# PART TWO

character = {
    'name': 'The Hound',
    'weapons': ['W-101', 'W-390'],
    'hemls': ['H-54'],
    'shields': ['S-13', 'S98']
}
for weapon in character['weapons']:
    print(weapon)

# character:
#     name: str
#     weapons: [P1, P2, P3]
character = {
    'name': 'The Hound',
    'weapons': [{
        'id': 'W-101',
        'name': 'Arakh of Khal Drogo',
        'price': 250,
        'category': 'Weapons'
    }, {
        'id': 'W-90',
        'name': 'Damascus Steel Widows Wail',
        'price': 960,
        'category': 'Weapons'
    }],
    'hemls': [{
        'id': 'H-54',
        'name': "The Hound's Helm",
        'price': 120,
        'category': 'Helms'
    }],
    'shields': [{
        'id': 'S-81',
        'name': 'Lannister Shield',
        'price': 310,
        'category': 'Shields'
    }, {
        'id': 'S-13',
        'name': 'Stark Infantry Shield',
        'price': 180,
        'category': 'Shields'
    },]
}

keys = ['weapons', 'hemls', 'shields']
result = {}
for key in keys:
    products = character[key]
    most_expensive_prod_in_key = {}

    for product in products:
        price = product ['price']
        if price > most_expensive_prod_in_key.get('price',0):
            most_expensive_product_in_key = product
    result[key] = most_expensive_product_in_key
print(result)
        #print("{cat}: {price}".format(cat = key, price=price))










