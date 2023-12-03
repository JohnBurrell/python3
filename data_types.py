# litteral assignment
first = "John"
last = "Burrell"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor function

# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# str concatenation

fullname = first + " " + last
print(fullname)
fullname += "!"
print(fullname)

# Cast number to string

decade = str(1980)
print(type(decade))
print(decade)

statement = "I like music from the " + decade + "s"
print(statement)

# multiple lines

multline = """
Hey, how's it going?

I was just checking.
                            More gumph.

"""
print(multline)

# Escaping special chars

sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# string methods

print(first)
print(first.lower())
print(first.upper())
print(first)
print(multline.title())
print(multline.replace("gumph", "stuff"))
print(multline)

print(len(multline))
multline += "                                  "
multline = "                  " + multline
print(len(multline))

print(len(multline.strip()))
print(len(multline.lstrip()))
print(len(multline.rstrip()))

print("")

# build a menu

title = "menu".upper()
print(title.center(20, "="))
print("coffee".ljust(16, ".") + "$1".rjust(4))
print("muffin".ljust(16, ".") + "$2".rjust(4))
print("cheesecake".ljust(16, ".") + "$4".rjust(4))

print("")

# string index values

print(first[0])
print(first[-1])
print(first[1:-1])
print(first[:])

# some methods return boolean

print(first.startswith("J"))
print(first.endswith("n"))

# Boolean data

myValue = True
x = bool(False)
print(type(x))
print(isinstance(myValue, bool))

# Numeric data types

# integer

price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float

gpa = 3.28
y = float(1.14)
print(type(gpa))

complex

comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# built-in functions for numbers

print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))

import math

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# cast a string as a number

zipcode = "77079"
zip_value = int(zipcode)
print(type(zip_value))
