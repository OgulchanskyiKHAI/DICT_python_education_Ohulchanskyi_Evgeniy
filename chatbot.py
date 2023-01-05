print("Hello! My name is Bart.")
print("I was created in 2022")
print("Please,remind your name.")
name = input("> ")
print("What a great name you have, {0}!.".format(name))
print("Let me guess your age.\nEnter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input(">"))
remainder5 = int(input(">"))
remainder7 = int(input(">"))
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is {0}; that a good time to start programming!".format(age))
print("Now I will prove to you that I can count to ane number you want.")
number = int(input((">")))
i = 0
while i != number+1:
    print("{0}!".format(i))
    i = i+1
print("Completed, have a nice day!")
print("How much will 5*5 be?")
print("1. 20")
print("2. 35")
print("3. 30")
print("4. 25")
number = int(input(">"))
while number !=4:
    print("Try again")
    number = int(input(">"))
    ...
print("Congratulations, have a nice day!")