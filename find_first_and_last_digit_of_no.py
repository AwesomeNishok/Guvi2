a=int(input("enter a number more than 1 digit"))
b=a
i=0
k=1
while a!=0:

 if a==0:
  break
 else:
  i=i+1
  a=a/10
j=b%10
print ("the last digit is:" ,j)
b=b/(10**(i-1))
print ("the first digit is:" ,b)
