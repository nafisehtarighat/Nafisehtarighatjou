def matrix(m,n):
    for i in range(m):
        for j in range(n):
            if i%2==1 :   
               if j%2==1:
                   print('#',end='')
               else:
                   print('*',end='')
            else:
                if j%2==0:
                     print('#',end='')
                else:
                     print('*',end='')
        print()    




m=int(input("the number of rows: "))
n=int(input("the number of columns: "))
matrix(m,n)
