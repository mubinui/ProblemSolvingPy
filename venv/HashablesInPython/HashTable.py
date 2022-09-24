# Hashtable or hashmap is kind of data structures that maps keys to its value pairs
# Dictionaries in python
my_dict = {1:'Mubin',2:'Samindra',3:'Superwoman'}
print(type(my_dict))
print(my_dict)
# another way of creating a dictionary in python
# your_dict = dict(key1:value1,key2:value2)
employee_details = {
    'Employee':{"Mubin":{'id':1,'Salary':30000000,'Designation':'CEO'}
                ,'Samindra':{'id':2,'Salary':50000000,'Designation':'Heart Specialist'}}

}
print(employee_details)
# Hash table operations
# Accessing hash tables
print(employee_details['Mubin'])