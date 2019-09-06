# 1. Ask a user for their first name and age. Print "[NAME] is [AGE] years old"
# userName = input("enter first name")
# userAge = int(input("Enter Age"))
# print(f'{userName} is {userAge}')

# 2. Ask the user to enter their age. Check if they entered a value between 0 and 125. If valid, print "REAL AGE". If invalid print “NOT A REAL AGE!!!”
# age = int(input("Enter your age"))
#
# if  age > 0 and age < 125:
#     print("REAL AGE")
# else:
#     print("NOT A REAL AGE!!!")

# 3. Use a for loop to print every 4 numbers from -50 to 50.

# for a in range(-50,51,4):
#     print(a)

# 4. Ask the user to enter a number to add to a total. Keep asking the user to enter a number until they enter 0. Afterward, print the total of all numbers entered.
# userInput = int(input("enter a number to add to a total"))
# while userInput != 0:
#     newuser = userInput
#     userInput = int(input("enter a number to add to a total"))
#     userAdd = userInput + newuser
#     print(userAdd)


# 5. Create an array of 4 names. Print one string that has all of the arrays separated by commas.
# namesArray = ['mark', 'paul', 'bob', 'ted']
# print(f'Names: {namesArray[0]}, {namesArray[1]}, {namesArray[2]}, {namesArray[3]}')

# 6. Create a function that’s passed three integer numbers. Print the sum of the first two numbers and return the product of the second two numbers.

# def prob6(a, b, c):
#     print(a+b)
#     print(b*c)
#
# prob6(8, 10, 22)


# # 7. Create the class Boardgame with name, price, pieceCount, and publisher properties/attributes. Create a class method that will change the price of the book. Outside of the class, create three objects of the class Boardgame. Print the three boardgame objects using the newly created objects.
#
# class Boardgame:
#     def __init__(self, name, price, pieceCount, publisher):
#         self.name = name
#         self.price = price
#         self.pieceCount = pieceCount
#         self.publisher = publisher
#
#     def __int__(self, newPrice):
#         self.newPrice = newPrice
#
#     def printAll(self):
#         print(f'Game: {self.name} Price:$ {self.price} Piece Count: {self.pieceCount} Publisher: {self.publisher}')
#
#
# game1 = Boardgame('Life', 19, 30, 'matel')
# game2 = Boardgame('jeopardy', 30, 20, 'parker bros')
# game3 = Boardgame('mouse trap', 10, 300, 'jerry')
#
# gamesArray = []
# gamesArray.append(game1)
# gamesArray.append(game2)
# gamesArray.append(game3)
#
# for eachElement in gamesArray:
#     eachElement.printAll()


# 8. Create a function that takes a string array and returns a string array with the letter 's' at the end of each element. Call the function.

stringArray = ["dove","poodle","frog","crimson"]
def pro8():
    stringArray.__delitem__(0)
    stringArray.__delitem__(1)
    stringArray.__delitem__(2)
    stringArray.__delitem__(3)
    stringArray.append('doves')
    stringArray.append('poodless')
    stringArray.append('frogs')
    stringArray.append('crimsons')

print(stringArray)
pro8()

# 9. Create a function that has a parameter of an integer array and returns only the positive numbers in the array. Call the function
# intArray =[-1,-12, 2, 3, 27]
# def prob9():
#     for k in range(intArray):
#         return k>0
# print(prob9())

#TODO: print the array???
# 10. Create a Puppy class. It should have properties name and color. Create a program that will ask a user to enter the name, then the color of a puppy until they enter 'q' to quit. Put each entry in an array.
# class Puppy:
#      def __init__(self, name, color):
#          self.name = name
#          self.color = color
#
#
# userInput = input("Enter Name")
# while userInput != "q":
#     userInput = input("Enter puppy color")
#
#
# userArray = []
# arrayList = [userArray.append(userInput)]
# print(arrayList)