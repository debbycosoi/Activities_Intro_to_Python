# a. First Name
firstName = "Debby"
# b. Last Name
lastName = "Cosoi"
# c. Favorite Color
favoriteColor = "Indigo"
# d. Favorite Meal
favoriteMeal = "Pizza"
# 2. Print out a sentence in Python that say “My First Name is x My Last Name is x My favorite color is x and my favorite meal is x”.
sentence = "My First Name is {0} My Last Name is {1} My favorite color is {2} and my favorite meal is {3}".format(firstName,lastName,favoriteColor,favoriteMeal)
print(sentence)
# 3. Repeat using:
# a. F-String
fString = f"My first name is {firstName} My Last Name is {lastName} My favorite color is {favoriteColor} and my favorite meal is {favoriteMeal}"
print(fString)
# b. Concatenation
concatenation = "My First Name is " + firstName +  " My Last Name is " + lastName + " My favorite color is " + favoriteColor + " and my favorite meal is " + favoriteMeal
print(concatenation)
# c. Argument by Position
position = "My First Name is {0} My Last Name is {1} My favorite color is {2} and my favorite meal is {3}".format(firstName,lastName,favoriteColor,favoriteMeal)
print(position)
#d. Argument by Name
name = "My first name is {firstName} My Last Name is {lastName} My favorite color is {favoriteColor} and my favorite meal is {favoriteMeal}".format(firstName="Debby",lastName="Cosoi", favoriteColor="Indigo", favoriteMeal="Pizza")
print(name) 