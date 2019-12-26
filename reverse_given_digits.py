a=int(input("enter a number more than 1 digit :"))
b=a
i=0
d=0
e=0
while a!=0:
  if a==0:
    break
  else:
     i=i+1
     a=a/10
j=i
while e<i:
 c=b%10
 d=d+(c*(10**(j-1)))
 b=b/10
 e+=1
 j-=1
print "the reversed digits are:" ,d