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
    # print(x, "----", y)

# UPDATION ##################################

my_dict['Chris'] = '004'
my_dict['Chris'] = '005'
my_dict['Jack'] = '004'
# print(my_dict)

#DELETION ###################################

my_dict.pop('Dave')
# print(my_dict)
my_dict.popitem()
# print(my_dict)

#CONVERT DICT TO DATAFRAME #################################

import pandas as pd

dataframe = pd.DataFrame(nested_dict['Employee'])
# print()
# print()
# print(dataframe)
# print()


stock_prices = {'6' : 340, '7' : 320, '8': 400, '9': 390, '10' : 310, '11': 297}
# print(type(stock_prices))

class HashTable:
    def __init__(self):
        self.size = 10
        self.arr = [[] for i in range(self.size)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.size

    def __setitem__(self, key, val):
       h = self.get_hash(key)
       found = False
       for idx, element in enumerate(self.arr[h]):
           if len(element) == 2 and element[0] == key:
               self.arr[h][idx] = (key, val)
               found = True
               break
       if not found:
            self.arr[h].append((key, val))

    def __getitem__(self, key):
       h = self.get_hash(key)
       for element in self.arr[h]:
           if element[0] == key:
               return element[1]

    def __delitem__(self, key):
       h = self.get_hash(key)
       for index, element in enumerate(self.arr[h]):
           if element[0] == key:
               del self.arr[h][index]
           

t = HashTable()
print(t.get_hash("march 6"))
print(t.get_hash("march 8"))
print(t.get_hash("march 9"))
print(t.get_hash("march 10"))
print(t.get_hash("march 17"))
t["march 6"] = 120
t["march 6"] = 78
t["march 8"] = 67
t["march 9"] = 4
t["march 10"] = 14
t["march 17"] = 459
print(t.arr)
print(t['march 6'])
# t.get_hash('march 6')
# t.get_hash('march 7')
# t.get_hash('march 8')
# t.get_hash('march 9')
# t.get_hash('march 10')
# t.get_hash('march 11')
# print(t.get_hash('6'))
# print(t.get_hash('7'))
# print(t.get_hash('8'))
# print(t.get_hash('9'))
# print(t.get_hash('10'))
# print(t.get_hash('11'))
# print(t.get_hash('sgsdfgsdfg'))
# print(t['dec 6'])
# print(t['march 6'])
del t['march 17']
del t['march 6']
print(t.arr)

