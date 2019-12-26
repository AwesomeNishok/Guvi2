a=int(input("enter a number more than 1 digit"))
i=0
while a!=0:

 if a==0:
  break
 else:
  i=i+1
  a=a/10
print(i)
