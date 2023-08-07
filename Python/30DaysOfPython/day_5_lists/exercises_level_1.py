# Exercises: Level 1

# 1 Declare an empty list
list1 = []
list2 = list()

# 2 Declare a list with more than 5 items
letters = ['a', 'b', 'c', 'd', 'e', 'd']

# 3 Find the length of your list
print(len(letters))

# 4 Get the first item, the middle item and the last item of the list
print(letters[0], letters[2], letters[-1])

# 5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Joaquin', 38, 1.80, 'married', 'Tucuman']

# 6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7 Print the list using print()
print(it_companies)

# 8 Print the number of companies in the list
print(len(it_companies))

# 9 Print the first, middle and last company
print(it_companies[0:7:3])

# 10 Print the list after modifying one of the companies
it_companies[2] = 'Tesla'
print(it_companies
)
# 11 Add an IT company to it_companies
it_companies.append('Youtube')
print(it_companies)

# 12 Insert an IT company in the middle of the companies list
it_companies.insert(4, 'Microsoft')
print(it_companies)

# 13 Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[2] = (it_companies[2].upper())
print(it_companies)

# 14 Join the it_companies with a string '#;  '
print('; # '.join(it_companies))

# 15 Check if a certain company exists in the it_companies list.
print('Youtube' in it_companies)

# 16 Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17 Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)

# 18 Slice out the first 3 companies from the list
first_3 = it_companies[0:3]
print(first_3)

# 19 Slice out the last 3 companies from the list
last_3 = it_companies[-3:]
print(last_3)

# 20 Slice out the middle IT company or companies from the list
middle_it = it_companies[4]
print(middle_it)

# 21 Remove the first IT company from the list
del it_companies[0]
print(it_companies)

# 22 Remove the middle IT company or companies from the list
del it_companies[3:5]
print(it_companies)

# 23 Remove the last IT company from the list
del it_companies[-1]

# 24 Remove all IT companies from the list
it_companies.clear()
print(it_companies)
# 25 Destroy the IT companies list
del it_companies

# 26Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined_list = front_end + back_end
print(joined_list)

# 27 After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = joined_list.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

