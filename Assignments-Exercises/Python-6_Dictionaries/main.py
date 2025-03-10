#Create a dictionary
dictionary = {'name': 'Wayne', 'age': 21}
print("Original dictionary:", dictionary)

# Add a city 
dictionary['city'] = 'Bataan'
print("Dictionary after adding an item:", dictionary)

# Update age
dictionary['age'] = 22
print("Dictionary after updating an item:", dictionary)

# Delete age
del dictionary['age']
print("Dictionary after removing an item:", dictionary)