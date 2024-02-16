
# Add Python to Dict
# Write a function that receives a dictionary as input, adds a new key-value pair saying "fav_language": "python" to it, and returns it! :D
#
# add_to_dictionary({"first_name": "jon", "last_name": "snow"})
#
# # {
# #   "first_name": "jon",
# #   "last_name": "snow",
# #   "fav_language": "python"
# # }


def add_to_dictionary(a_dictionary):
    a_dictionary.update({"fav_language":"python"})
    return a_dictionary
    pass
add_to_dictionary({"first_name": "jon", "last_name": "snow"})

