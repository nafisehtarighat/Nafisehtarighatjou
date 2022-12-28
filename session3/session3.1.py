mylist=[]
n=int(input("the length of the list:"))
for i in range(n):
  num=int(input("number:"))
  mylist.append(num)
i=0  
while i<len(mylist):
  j=i+1
  while j<len(mylist):
    if mylist[i]==mylist[j]:
      mylist.pop(j)
      j=j-1
    j=j+1
   
  i=i+1
  
print(mylist)


  
