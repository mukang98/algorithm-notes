#%%
# ================================================================= #
#                       1. Regular Expression                       #
# ================================================================= #
# A Regular Expression (regex or regexp) is a sequence of characters that forms a search pattern.
# It is used for string matching and manipulation, such as searching for specific text, replacing text, or extracting data from strings.
# Regular expressions are a powerful tool in text processing, allowing you to define complex patterns using metacharacters like '.', '*', '^', '$', and more.
#%%
# Introduce its basic usage through some examples
"""
E.g.1 
    A regex matches the string starts as "a" and ends at "z"
"""
import re
sample_input_1 = [
    "abz", 
    "applez", 
    "a123z", 
    "az"
]
pattern1 = r'^a\w*z$'
for item in sample_input_1:
    result = re.match(pattern1, item) # re.match() requires the begining of the string matches the regex.
    print(result)

# %%
"""
E.g.2
    A regex extracts all continuous numbers
"""
import re
sample_input_2 = [
    "The price is 123 dollars and 45 cents.",
    "My phone number is 9876543210.",
    "There are 24 hours in a day."
]
pattern2 = r'\d+'
for item in sample_input_2:
    result = re.findall(pattern2, item) # Find all occurrences of numbers in the current string using the regular expression and return a list of matched numbers
    print(result)
# %%
"""
E.g.3
    A regex test and verify if given string is a valid email address.
"""
import re
sample_input_3 = [
    "test@example.com",
    "user.name@domain.co",
    "user_name@domain.com",
    "invalid-email@com",
    "@no-domain.com"
] #match the first three but not the last two.

# pattern3 = r'^\w+[@]\w+\.(co|com)$'  \w matches only letters, numbers, and underscores, so it won't match email addresses that contain '.' in the local part (before the @ symbol).
pattern3 = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(co|com)$'
for item in sample_input_3:
    result = re.match(pattern3, item) 
    print(result)
# %%
"""
E.g.4
    Replace all instances of 'cat' in a string with 'dog' using regex.
"""
import re
sample_input_4 = [
    "The cat sat on the cat mat.",
    "Concatenate the cat and the dog."
]
pattern4 = r'cat'
for item in sample_input_4:
    result = re.sub(pattern4, "dog", item)  #Use re.sub() to replace 'cat' with 'dog'. The 'count' parameter provides the option to limit the number of replacements.
    print(result)
# %%
"""
E.g.5
    A regex extracts the file extension from a filename string.
""" 
import re
sample_input_5 = [
    "document.pdf",
    "archive.tar.gz",
    "image.jpeg",
    "no_extension"
]

# Regular expression pattern to match file extensions
pattern5 = r'\.([a-zA-Z0-9]+)$'
#Using capture groups allows you to extract specific parts of regular expression matches, 
#while not using capture groups can only obtain complete matching results.
for file_name in sample_input_5:
    match = re.search(pattern5, file_name)
    if match:
        # Extract and print the file extension without the dot
        print(match.group(1))
    else:
        # Print 'No match' if there is no file extension
        print('No match')


# %%
