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