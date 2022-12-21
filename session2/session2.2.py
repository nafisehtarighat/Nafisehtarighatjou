import random
while True:
    key=input("roll the dice = press the 'R' key or exit = press the 'E' key--> ")
    if key=="E" :
        break
    elif key=="R" :
        dice=random.randint(1,6)
        print(dice)
        while dice==6 :
            input("Roll the dice one more time = press any key--> ")
            dice=random.randint(1,6)
            print(dice)
    else:
        print("invalid key")



     
         
