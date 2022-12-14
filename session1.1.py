import math
num1=float(input("first number :"))
op=input("operator:")
if op=="+" or op=="-" or op=="*" or op=="/" or op=="radical" or op=="sin" or op=="cos" or op=="tan" or op=="cot" or op=="!" :
    if op=="radical" :
        if num1>=0 :
            print(math.sqrt(num1))
        else :
            print("invalid input")
    elif op=="sin" :
        print(math.sin(math.radians(num1)))
    elif op=="cos" :
        print(math.cos(math.radians(num1)))
    elif op=="tan" :
        print(math.tan(math.radians(num1)))
                    
    elif op=="cot" :
        x=math.tan(math.radians(num1))
        if x!=0 :
          print(1/x)
        else :
          print("invalid input")  
    elif op=="!" :      
        if num1>=0 and num1==int(num1):  
            print(math.factorial(num1))
        else :
            print("invalid input")
    else:
        num2=float(input("second number :"))
        if op=="+" :
            print(num1+num2)
        elif op=="-" :
            print(num1-num2)
        elif op=="*" :
            print(num1*num2)
        else: 
            if num2!=0 :
                print(num1/num2)
            else:
                print("error")
         
else:
    print("invalid operator")
        
