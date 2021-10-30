#Arithmetic Bot made by @Umairka123
#Enjoy!
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Like to always have this in my cod
import datetime as dt
import time

current_date = dt.date.today()
print(current_date)

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time: ", current_time)

#One day I'm gonna learn how to make a GUI!!!
username = print("Hello welcome to Arithmetic, the time is " + str(current_time) + " ! Please enter you username: ")

username = input()


print("Cool! Lets start " + username + "!")
time.sleep(0.5)

print("Arithmetic is all about testing your mathmatic!")
time.sleep(0.7)

#Loop until they answer with y___ or n____
while True:

   answer = input('Do you want to continue?:')

   if answer.lower().startswith("y"):

      print("Ok, Lets start!" + username)

      break

   elif answer.lower().startswith("n"):

      print("Ok, bye. Have a good day!")
     
      
#Maybe we could try three numbers one day!
print("give me two numbers!")

num1 = input("Number 1: ")

num2 = input("Number 2: ")


sumuno = int(num1) + int(num2)

#If you use a plus then it won't concanate (Note to self: ALWAYS USE A COMMA (,) FOR INT)

#Addition
print("If you add them together you get: " , sumuno )
time.sleep(0.7)

sumduo = int(num1) * int(num2)
#Multiplication
print("If you multiply your numbers you get: " , sumduo)
time.sleep(0.7)

#Squaring the number's
sumtres = int(num1)** 2
print("If you square " + num1 + " you get: " , sumtres)
time.sleep(0.7)

sumfour = int(num2)** 2
print("If you square " + num2 + " you get: " , sumfour)
time.sleep(0.7)

#Time for the User test part!

print("Ok " + username + " time for me to test your Arithmetic ability!")


print("Let's start of easy!")

while True:

   ans1 = input('What is 20-10?')

   if ans1 == ("10"):

      print("Well done that's right " + username + "!")

      break

   else: print("Sorry that's wrong " + username + " try again!")

while True:

   ans2 = input('What is 88-24?')

   if ans2 == ("64"):

      print("Well done that's right " + username + "!")

      break

   else: print("Sorry that's wrong " + username + " try again!")

while True:

   ans3 = input('What is 245-189?')

   if ans3 == ("65"):

      print("Well done that's right " + username + "!")

      break

   else: print("Sorry that's wrong " + username + " try again!")

while True:

   ans4 = input('What is 12 x 16?')

   if ans4 == ("192"):

      print("Well done that's right " + username + "!")

      break

   else: print("Sorry that's wrong " + username + " try again!")

while True:

   ans5 = input('What is 268 x 10?')

   if ans5 == ("2680"):

      print("Well done that's right " + username + "!")

      break

   else: print("Sorry that's wrong " + username + " try again!")

while True:

   ans6 = input("What is 256 x 654")

   if ans6 == ("167424"):
      print("You're doing great " + username + "!")

   else:
       print("Sorry that's wrong " + username + ", but don't worry! Try again and you'll get it this time!")

print("Thank you " + username + " for playing my Arithmetic Game! Please come again!")
time.sleep(20)