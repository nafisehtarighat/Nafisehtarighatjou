import random
mylist=[]
n=int(input("the length of the array: "))
s=0
e=2*n
num_random=random.randint(s,e)
mylist.append(num_random)
i=1
while i<n :
    num_random=random.randint(s,e)
    count_num=mylist.count(num_random)
    if count_num==0 :
        mylist.append(num_random)
        i=i+1
print(mylist)
