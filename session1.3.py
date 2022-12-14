input("name :")
input("fmaily :")
g1=float(input("first grade :"))
g2=float(input("second grade :"))
g3=float(input("third grade :"))
ave=(g1+g2+g3)/3
if ave>=17 :
    print("status : GREAT")
if 12<ave<=17 :
    print("status : NORMAL")
if ave<12 :
    print("status : FAIL")
    
