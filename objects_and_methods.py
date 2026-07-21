# Let's first re-create a variable or two
my_integer = 10
my_str = "Hello world"
# I told you before that t you can always see the type of a variable using type().
type(my_integer)
type(my_str)

# What is stored inside these objects?
my_str.upper # upper is a METHOD that is attached to all the objects of class string
# A method is like a function, so it needs to be CALLED. How do we call a function again?
# We put () after it.
my_str.upper() # Returning the upper, capitalized version of the string.
my_str.upper() # What does it mean return a copy?
# It means the original string is unchanged:
my_str
# let's try another one
my_str.lower()
# What else is in there?
my_str.endswith('!') # Does not end with a '!'
my_str.endswith('orld') # Returns true!
# Methods are a way of pairing functions to specific types of objects.

# Some objects have other things than methods: Properties.
# Properties are information about the objects that was created.
my_integer.denominator # White wrenches are properties of the object
my_integer.numerator # Do we put ()? No.
# Properties are only meant to be read. They don't do anytihng. They just exist.
# and does not do anything, it is probably a property.
# But to be sure: look at the icon.

# Let's check a few more methods that exist on a string
my_name = "jamie lin"
print(my_name.capitalize())
print(my_name.title())
print(my_name.count('e'))
print(my_name.replace('a', 'x'))
# Methods are natural ways of (i) encspsulating functions that are relevent
# to a type of object and of (ii) acting upon the object.

n_chars = len(my_name)
print(n_chars) # The number of characters in my name
# This is a function. it is not called from within the object using the dot, 
# It stands alone.
my_upper_name = my_name.upper() # This is a method. You are calling it with the dot,
# from within the object. It is connected to my_name.

# What will this line do?
print(my_name.lower) # We reached inside the box for the method, but we did not run
# it yet! To call it, you need to add perenthesis after.

my_age = 39
print(my_age.numerator)
print(my_age.denominator)
print(my_age.as_integer_ratio) # Here I reached for a method
# If I want this method to run, I need to call it!
print(my_age.as_integer_ratio())

# Let's see a few more things about methods!
greeting = "hello welcome to class"
# Next, I am going to capitalize this greeeting
print(greeting.upper())
print(greeting) # Still lower case. Why?
# Most methods RETURN a new value. Think of them as a machine that copies the
# original, modifies it, and returns it to you.
# The original is not changed
# In jargon, we say, the methods do not MUTATE the original object.
user_input = "  quentin.andre@colorado.edu "
# My mission: Check that the email entered by the user is a .edu email.
bad_solution = user_input.endswith('.edu') # Returns False, white spaces are ruining everything.
# Multiple steps:
trim_input = user_input.strip()
print(trim_input)
good_solution = trim_input.endswith('.edu')
print(good_solution)
# Now, can we type a BETTER solution?
better_solution = user_input.strip().endswith('.edu')
# Comprehension check!
is_this_true = user_input.strip().upper().endswith('.edu')
this_is_true = user_input.strip().upper().endswith('.EDU')
is_this_true
this_is_true
# Could we do that?
user_input.strip().upper().endswith('.EDU') # We cannot do that, since print() isnot 
# a method that we can call on the resulting obejct.

# What about that?
user_input.strip().endswith('.edu').upper() # The upper method does not exist on a bool object
# WHich is precisely what endswith will reurn.
# Nice segue into some of the errors that can pop up:
user_input.shout() # AttributeError: WHen you attempt to reach for a method or property
# that does not exist on an object of a certain type.

my_age.denominator() # I am attempting to call an attribute as if it were a method

# There are more than four different types of objects in Python.
# I'm going to show you how objects of different types are created.

# First, to create an int:
my_int = 10
# ... or a string:
my_str = 'Something with quotes'
# To create other objects, you need to call an object factory that will create the object for you.
# Here, we will work with an object called Decimal, that allows you to create decimal numbers
# with exact representations (no floating point error):

from decimal import Decimal # Trust me bro, not going to cover this one for you.

a = Decimal('.1') # Here, i created a decimal object equal to .1.
print(type(a))
b = Decimal('.2') # I am creating another decimal objects.
# You will recognize object factories from their capital letter and their green color:
# Now that I have a new object, I can see what kind of methods and properties they contain:
a # With the dot notation
# What is the interest of this Decimal object?
print(a + b)
print(a + b == 0.3) # FALSE
print(a + b == Decimal('.3'))
# An example of creating a new type of object and reaching for its method