# Printing "Hello World":
print("Hello World")

# Printing "Hello Noelle!" with the name in a variable:
name = "Noelle"
print("Hello", name)  # with a comma
print("Hello " + name)  # with a +

# Printing "Hello 42!" with the number in a variable:
number = 42
print("Hello", number)  # with a comma
print("Hello " + str(number))  # with a + -- this one should give us an error!

# Printing "I love to eat sushi and pizza." with the foods in variables:
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}.".format(fave_food1, fave_food2))  # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.")  # with an f-string

