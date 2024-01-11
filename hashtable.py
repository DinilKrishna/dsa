my_dict = {'Dave':'001', 'Ava':'002', 'Joe':'003'}
# print(my_dict)
# print(type(my_dict))

new_dict = dict()
# print(new_dict)
new_dict = dict(Dave = '001', Ana = '002')
# print(new_dict)

nested_dict = {'Employee' : {'Arun' : 
                                    {'ID' : '001', 'Salary' : '20000', 'Designation' : 'Team Lead'},
                             'Saju' : 
                                    {'ID' : '002', 'Salary' : '30000', 'Designation' : 'Associate'}
                            }
              }
# ACCESSING ##################################

# print(nested_dict)

# print(nested_dict['Employee']['Arun'])
# print(my_dict.get('Ava'))

# for x,y in my_dict.items():
#     print(x, "----", y)

# UPDATION ##################################

my_dict['Chris'] = '004'
my_dict['Chris'] = '005'
my_dict['Jack'] = '004'
print(my_dict)

#DELETION ###################################

my_dict.pop('Dave')
# print(my_dict)
# my_dict.popitem()
print(my_dict)

#CONVERT DICT TO DATAFRAME #################################

import pandas as pd

dataframe = pd.DataFrame(nested_dict['Employee'])
print()
print()
print(dataframe)
print()