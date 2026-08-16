# No restriction for '' or "" as can be used as per need
msg = 'Test Python'
msg2 = "Test Python 2"

# For printing in next line use """
nextLine = """We are about to print this string
in next line."""

# Length of string
length = len(nextLine)

# Accessing by index as indexing start from 0
# False index (which doesn't exists) will return index error
# print(nextLine[3])

# We can also access some specific text with mentioned range
# print(nextLine[2:9])

# By default range will start from 0 if start point is not specified
# print(nextLine[:10])

# By default range will take it to the end of text if end point is not specified
# print(nextLine[10:])

# Built int methods for string values
# Lower and upper
# print(msg.lower())
# print(msg.upper())

# Counting for specific word or character in whole string
# Argument passed in count will be case-sensitive
# print(msg.count('test')) # This will result in 0 cuz 'test' != 'Test'
# print(nextLine.count('t'))

# To find out the starting index of specific word in whole string
# This method's argument will also be case-sensitive
# If argument is not in the string, it will return -1
# print(msg.find('Python')) # This will print 5 cuz this word starts from index 5

# Replacing the words
# Replace method returns a new string instead of updating the original one
# In order to update original one, we have to assign new value to new variable or re-assign to original variable itself
# msg.replace('test', 'Hi there') # This worked but will not show new result
# new_msg = msg.replace('Test', 'Hi there')
# Re-assign to original one
# msg = msg.replace('Test', 'Replaced to')
# print(msg)

# String Concatination
# Basic way but not good practice for complex strings
greet = 'Hi'
name = 'Python'

concat = greet + ', ' + name

# Good practice for complex strings using f strings
new_concat = f'{greet}, {name}. Welcome!'
print(new_concat)

# If we want to check which methods are available for us to use for strings.
# Use dir(stringName)
print(dir(msg))

# For overall detailed context use help function
# help(dataType)
print(help(str))
