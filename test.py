# This is a testing file for giving a general idea of how to use the module 'utlify'.

# I know some might argue that the main code has some examples on most functions 
# But some people don't like it and get lost so we had to make an independent file for testing.
# Hopefully everyone's happy now

from utilify import *

# (I made this so i don't have to call the name 'utilify' everytime i call a function from it)



"""Part 1: classes"""

# ----------------------------------------------
# First: variable class
# This is supposed to help you handle variables and edit them easily
# ----------------------------------------------
my_var = "hellon"

# let's delete the useless 'n':
print(variable.Idelete(my_var, -1)) # hello
# another way:
print(variable.delete(my_var, "n", 1)) # hello

print(variable.insert("l", "helo", 2)) # hello 

print(variable.replace("pytkon", 3, "h")) # python

print(variable.random_int(1, 20)) # a random integer between 1-20



print("-" * 42)
# ----------------------------------------------
# 2nd class: strings class
# it is used for strings-related utilities
# ----------------------------------------------

print(strings.is_palindrome("wow")) # True

print(*strings.lower_letters) # all lowercase English letters

print(*strings.upper_letters) # all uppercase English letters

print(*strings.ascii_symbols) # all ASCII symbols

print(strings.remove_letters("iwaltlchi", "l", "i")) # watch

"""Part 2: other functions"""
# ----------------------------------------------
# Other utilizer functions to your code
# ----------------------------------------------
print("-" * 42)

print(are_close("Drama", "Trauma", threshold=0.90, minimum=0.70, get_ratio=False)) # None

print(are_close("Drama", "Trauma", 0, 0, get_ratio=True)) # 72%

flash_text("Hello world", delay=1)

dic: dict = {
	"one": 1,
	"two": 2,
	"three": 3
}
flash_items(dic, delay=0.5)

Sprint(dic, delay=0.5, ending="\n")

text = "python"

print(get_index("h", text)) # 3
print(get_location(4, text)) # o

print(auto_correct("jvaa", ("java", "Assembly"), None)) # java

@timer
def function():
	for i in range(99999):
		print("hello", i)
function() # 1.0xxx

print(getabbr("information & communication tech")) # ICT
print(getabbr("world health org ")) # 🌐WHO