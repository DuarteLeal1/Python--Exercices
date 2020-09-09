import random
print("In this game you only need to write 4 numbers and then one of them will be drawn.")
n1 = int(input("Write a number: "))
n2 = int(input("Write other number: "))
n3 = int(input("Again... : "))
n4 = int(input("One more time... : "))
numberlist = [n1, n2, n3, n4]
numberchoised = random.choice(numberlist)
print(f"The chosen number is {numberchoised}.")
