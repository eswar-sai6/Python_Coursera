# If you are not sure what class (data type) a value falls into, Python has a function called type which can tell you.
print(type("Hello, World!"))  # string
print(type(17))  # int
print("Hello, World")  # print Hello, World
print(type(3.2))  # float
# What about values like "17" and "3.2"? They look like numbers, but they are in quotation marks like strings.
print(type("17"))  # output is str
print(type("3.2"))  # output is str

# They’re strings!
# Strings in Python can be enclosed in either single quotes (') or double quotes ("), or three of each (''' or """)
print(type('This is a string.'))
print(type("And so is this."))
print(type("""and this."""))
print(type('''and even this...'''))
# Double-quoted strings can contain single quotes inside them, as in "Bruce's beard", and single quoted strings can
# have double quotes inside them, as in 'The knights who say "Ni!"'. Strings enclosed with three occurrences of
# either quote symbol are called triple quoted strings. They can contain either single or double quotes:
print('''"Oh no", she exclaimed, "Ben's bike is broken!"''')
# Triple quoted strings can even span multiple lines:
print("""This message will span
several lines
of the text.""")
# Python doesn't care whether you use single or double quotes or the three-of-a-kind quotes to surround your strings.
# Once it has parsed the text of your program or command,
# the way it stores the value is identical in all cases,
# and the surrounding quotes are not part of the value.
print('This is a string.')
print("""And so is this.""")
# So the Python language designers usually chose to surround their strings by single quotes.
# What do you think would
# happen if the string already contained single quotes?
# When you type a large integer, you might be tempted to use commas between groups of three digits, as in 42,000.
# This is not a legal integer in Python, but it does mean something else, which is legal:
print(42500)
print(42,500)
print(42, 17, 56, 34, 11, 4.35, 32)
print(3.4, "hello", 45)
