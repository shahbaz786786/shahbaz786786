import random
number=input(" Please inter the number here ")
if number.isdigit():
    number=int(number)
    if number<=0:
        print("Please Enter the Number above the 0 ")
        quit()
else:
    print("Please Enter the Digit for the next time ")
    quit()

random_number=random.randint(0,number)



while True:

    guess_number = input("Enter guess number ")

    if guess_number.isdigit():
        guess_number = int(guess_number)
    else:
        print("Please Enter the Digit for the next time ")
        quit()

    if guess_number==random_number:
        print("You got it!")
        break
    else:
        print("Please enter again ")
        continue