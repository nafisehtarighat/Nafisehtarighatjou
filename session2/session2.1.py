import random
pc_random=random.randint(0,20)
user_number=int(input("enter your number:"))
counter=1
while user_number!=pc_random :
    if pc_random>user_number :
        print("up")
    if pc_random<user_number :
        print("down")
    user_number=int(input("enter your number:"))
    counter=counter+1
print("random number is:",pc_random)
print("Number of guesses:",counter)
