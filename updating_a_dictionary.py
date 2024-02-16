#
# Updating a Dictionary
# Update the dictionary provided in the editor making the following changes:
#
# Update the name from "RMOTR" to "rmotr.com"
# Include a new key email with the value 'questions@rmotr.com'
# Update the list of courses to include "Django Web Development"

rmotr_dict = {
    'name': 'RMOTR',
    'courses': ['Intro to Python', 'Advanced Python'],
}

rmotr_dict['name']='rmotr.com'
rmotr_dict['email']='questions@rmotr.com'
rmotr_dict['courses'].append("Django Web Development")

print(rmotr_dict)

for k,v in rmotr_dict.items():
    print(k + " " + str(v))

