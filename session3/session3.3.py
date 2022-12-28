def equation(a,b,c):
    import math
    
    if a==0:
        print("It is not a quadratic equation")
    else:    
        delta=b**2-4*a*c
        if delta>0 :
            x1=(-b+math.sqrt(delta))/(2*a)
            x2=(-b-math.sqrt(delta))/(2*a)
            print("The quadratic equation has two real roots:\n",x1,'  ',x2)
        elif delta==0:
            x=-b/(2*a)
            print("The quadratic equation has double roots:\n",x)
            
        else: 
            print("The quadratic equation has no real roots!")


            
a=int(input("a; "))
b=int(input("b: "))
c=int(input("c: "))
equation(a,b,c)
