# 1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
strings_1 = ['Thirty', 'Days', 'Of', 'Python']
result = ' '.join(strings_1)
print(result)

# 2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
strings_2 = ['Coding', 'For', 'All']
result_2 = ' '.join(strings_2)
print(result_2)

# 3 Declare a variable named company and assign it to an initial value "Coding For All".
company = result_2

# 4 Print the variable company using print().
print(company)

# 5 Print the length of the company string using len() method and print().
print(len(company))

# 6 Change all the characters to uppercase letters using upper() method.
print(company.upper())

# 7 Change all the characters to lowercase letters using lower() method.
print(company.lower())

# 8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9 Cut(slice) out the first word of Coding For All string.
first_word = company[:6]
print(first_word)

# 10 Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index('Coding'))
print('Coding' in company)

# 11 Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))

# 12 Change Python for Everyone to Python for All using the replace method or other methods.
print(company.replace('Coding', 'Python').replace('All', 'Everyone'))

# 13 Split the string 'Coding For All' using space as the separator (split()) .
print(company.split(' '))

# 14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
tech_companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(tech_companies.split(','))

# 15 What is the character at index 0 in the string Coding For All.
print(company[0])

# 16 What is the last index of the string Coding For All.
print(company[-1])

# 17 What character is at index 10 in "Coding For All" string.
print(company[10])

# 18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
acron = 'Python For Everyone'
print(acron.replace('Python','P').replace('For','F').replace('Everyone','E'))

# 19 Create an acronym or an abbreviation for the name 'Coding For All'.
print(company[0],company[7], company[11])

# 20 Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))

# 21 Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))

# 22 Use rfind to determine the position of the last occurrence of l in Coding For All People.
last_occur = 'Coding For All People'
print(last_occur.rfind('l'))

# 23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence_because = 'You cannot end a sentence with because because because is a conjunction'
sub_be = 'because'
print(sentence_because.index(sub_be))

# 24 Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence_because.rindex(sub_be))

# 25 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence_because[31:55])

# 26 Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence_because.find('because'))

# 27 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 28 Does ''Coding For All' start with a substring Coding?
print(company.startswith('Coding'))

# 29 Does 'Coding For All' end with a substring coding?
sub_co = 'coding'
print(company.endswith(sub_co))

# 30 '   Coding For All      '  , remove the left and right trailing spaces in the given string.
trailing_spaces = '   Coding For All      '
print(trailing_spaces)
print(trailing_spaces.strip(' '))

# 31 Which one of the following variables return True when we use the method isidentifier():
    # 30DaysOfPython
    # thirty_days_of_python
    # numer 2
ident_1 = '30DaysOfPython'
ident_2 = 'thity_day_of_python'
print(ident_1.isidentifier())
print(ident_2.isidentifier())

# 32 The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libra = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(libra))

# 33 Use the new line escape sequence to separate the following sentences.
    # I am enjoying this challenge.
    # I just wonder what is next.
print('I am enjoying this challenge.\nI just wonder what is next.')
# 34 Use a tab escape sequence to write the following lines.
    # Name      Age     Country   City
    # Asabeneh  250     Finland   Helsinki
print('Name\tAge\tCountry\t\tCity\nJoaquin\t38\tArgentina\tTucuman')
#  35 Use the string formatting method to display the following:
    # radius = 10
    # area = 3.14 * radius ** 2
    # The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
circle_string =('The area of a circle with radius {} is {:.2f} meters square.').format(radius, area)
print(circle_string)

#  36 Make the following using string formatting methods:
    # 8 + 6 = 14
    # 8 - 6 = 2
    # 8 * 6 = 48
    # 8 / 6 = 1.33
    # 8 % 6 = 2
    # 8 // 6 = 1
    # 8 ** 6 = 262144
a = 8
b = 6    
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))
