# PARAMETERS AND ARGUMENTS 

#A PARAMETER is a variable in the definition of a function.
#An ARGUMENT is the value being passed into a function call.
#A function DEFINITION begins with def and contains the entire following indented block.
#And function CALLS are the places a function is invoked, with parentheses, after its definition

# NONE

# None is a special value in Python. It is unique (there can’t be two different Nones) and immutable (you can’t update None or assign new attributes to it).
# None is falsy, meaning that it evaluates to False in an if statement.
# None is also unique, which means that you can test if something is None using the is keyword.

def no_return():
  print("You've hit the point of no return")
  # notice no return statement

here_it_is = no_return()

print(here_it_is)
# Prints out "None"

# DEFAULT ARGUMENTS

# Function arguments are required in Python. So a standard function definition that defines two parameters requires two arguments passed into the function.

# The required parameters need to occur before any parameters with a default argument.

# Raises a TypeError
def create_user(is_admin=False, username, password):
  create_email(username, password)
  set_permissions(is_admin)

# KEYWORDS ARGUMENTS
# We use keyword arguments by passing arguments to a function with a special syntax that uses the names of the parameters. This is useful if the function has many optional default arguments or if the order of a function’s parameters is hard to tell.

# UNPACKING MULTIPLE RETURNS
# In Python we can return multiple pieces of data by separating each variable with a comma:

def multiple_returns(cool_num1, cool_num2):
  sum_nums = cool_num1 + cool_num2
  div_nums = cool_num1 / cool_num2
  return sum_nums, div_nums

def scream_and_whisper(text):
    scream = text.upper()
    whisper = text.lower()
    return scream, whisper

the_scream, the_whisper = scream_and_whisper("Let's scream and whisper!")
print(the_scream, the_whisper)

# POSITIONAL ARGUMENT PACKING
#We don’t always know how many arguments a function is going to receive, and sometimes we want to handle any possibility that comes at us. Python gives us two methods of unpacking arguments provided to functions. The first method is called positional argument unpacking, because it unpacks arguments given by position. Here’s what that looks like:

def shout_strings(*args):
  for argument in args:
    print(argument.upper())

shout_strings("hi", "what do we have here", "cool, thanks!")
# Prints out:
# "HI"
# "WHAT DO WE HAVE HERE"
# "COOL, THANKS!"

# Our parameter args is a tuple of all of the arguments passed. In this case args has three values inside, but it can have many more (or fewer).

def truncate_sentences(length, *sentences):
  for sentence in sentences:
    print(sentence[:length])

truncate_sentences(8, "What's going on here", "Looks like we've been cut off")
# Prints out:
# "What's g"
# "Looks li"

#Python doesn’t stop at allowing us to accept unlimited positional parameters, it gives us the power to define functions with unlimited keyword parameters too. The syntax is very similar, but uses two asterisks (**) instead of one.

def arbitrary_keyword_args(**kwargs):
  print(type(kwargs))
  print(kwargs)
  # See if there's an "anything_goes" keyword arg
  # and print it
  print(kwargs.get('anything_goes'))

arbitrary_keyword_args(this_arg="wowzers", anything_goes=101)
# Prints "<class 'dict'>
# Prints "{'this_arg': 'wowzers', 'anything_goes': 101}"
# Prints "101"



































