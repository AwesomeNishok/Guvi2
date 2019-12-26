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
temp=j
j=b
b=temp

c=c%(10**(i-2))
0
c=c%(10**(i-2))
c=c*10+j
c=(b*(10**(i-1)))+c
print "the swapped soln is:",c


