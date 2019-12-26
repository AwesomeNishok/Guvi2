a=int(input("enter a number more than 1 digit :"))
b=a
c=a
i=0
while a!=0:

 if a==0:
  break
 else:
  i=i+1
  a=a/10
j=b%10
print "the last digit is:" ,j
b=b/(10**(i-1))
print "the first digit is:" ,b
sum=j+b
print("the sum of first and last digit of the given no.:" ,sum)

