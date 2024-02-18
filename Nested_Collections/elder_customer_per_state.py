# # Eldest customer per state
# # With the same structure as before, now you need to write a function that finds the eldest customer per state. Example:
# #
# customers = {
#     'UT': [{
#         'name': 'Mary',
#         'age': 28
#     }, {
#         'name': 'John',  # Eldest
#         'age': 31
#     }, {
#         'name': 'Robert',
#         'age': 16
#     }],
#     'NY': [{
#         'name': 'Linda',  # Eldest (only customer)
#         'age': 71
#     }],
#     'CA': [{
#         'name': 'Barbara',
#         'age': 15
#     }, {
#         'name': 'Paul',
#         'age': 18
#     }, {
#         'name': 'Helen',  # Eldest
#         'age': 29
#     }]
# }
# results = eldest_customer_per_state(customers)
# print(results)
# Prints:
#
# expected_result = {
#     'UT': {
#         'name': 'John',
#         'age': 31
#     },
#     'NY': {
#         'name': 'Linda',
#         'age': 71
#     },
#     'CA': {
#         'name': 'Helen',
#         'age': 29
#     }
# }

customers = {
    'UT': [{
        'name': 'Mary',
        'age': 28
    }, {
        'name': 'John',  # Eldest
        'age': 31
    }, {
        'name': 'Robert',
        'age': 16
    }],
    'NY': [],
    'CA': [{
        'name': 'Barbara',
        'age': 15
    }, {
        'name': 'Paul',
        'age': 18
    }, {
        'name': 'Helen',  # Eldest
        'age': 29
    }]
}

def eldest_customer_per_state(customers):
    states = list(k for k in customers)
    result = {}
    for st in states:
        eldest_customer_age = {}
        cust = customers[st]

        for c in cust:
            highest = c['age']
            if highest > eldest_customer_age.setdefault('age',0):
                eldest_customer_age = c

        result[st] = eldest_customer_age
        for k,v in result.items():
            if v == {}:
                print()
                result[k] = None


        #print(result)
    return result

    print(eldest_customer_per_state(customers))




# keys = ['weapons', 'hemls', 'shields']
# result = {}
# for key in keys:
#     products = character[key]
#     most_expensive_prod_in_key = {}
#
#     for product in products:
#         price = product ['price']
#         if price > most_expensive_prod_in_key.get('price',0):
#             most_expensive_product_in_key = product
#     result[key] = most_expensive_product_in_key
# print(result)

print(eldest_customer_per_state(customers))
