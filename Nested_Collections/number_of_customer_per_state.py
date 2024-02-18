# Number of customers per state
# Customers are expressed as a dictionary, divided by state. Each key represents a state. Example:
#
customers = {
    'UT': [{
        'name': 'Mary',
        'age': 28
    }, {
        'name': 'John',
        'age': 31
    }, {
        'name': 'Robert',
        'age': 16
    }],
    'NY': [{
        'name': 'Linda',
        'age': 71
    }],
    'CA': [{
        'name': 'Barbara',
        'age': 15
    }, {
        'name': 'Paul',
        'age': 18
    }]
}
# Each state contains a list with all the customers. A single customer is represented as a dictionary with only two keys, name and age.
#
# Write a function number_of_customers_per_state that receives a customers dictionary and calculates the number of customers per state. The result will be a new dictionary, with each key containing a state and the count as the associated value.
#
# Example:
#
# customers = {
#     'UT': [{
#         'name': 'Mary',
#         'age': 28
#     }, {
#         'name': 'John',
#         'age': 31
#     }, {
#         'name': 'Robert',
#         'age': 16
#     }],
#     'NY': [{
#         'name': 'Linda',
#         'age': 71
#     }],
#     'CA': [{
#         'name': 'Barbara',
#         'age': 15
#     }, {
#         'name': 'Paul',
#         'age': 18
#     }]
# }
# result = number_of_customers_per_state(customers)
# print(result)
# Prints:
#
# expected_result = {
#     'UT': 3,
#     'NY': 1,
#     'CA': 2
# }


def number_of_customers_per_state(customers_dict):
    state_list = []
    total_per_state = {}
    for k,v in customers_dict.items():
        state_list.append(k)
        if v != None:
            total_per_state[k]=len(v)
        else:
            total_per_state[k] = 0
    print(total_per_state)
    return (total_per_state)
    pass

number_of_customers_per_state(customers)
