a=int(input("enter a number more than 1 digit :"))
b=a
i=0
c=1
d=0
while a!=0:
  if a==0:
    break
  else:
     i=i+1
     a=a/10
while d<i:
 c=c*(b%10)
 d+=1
 b=b/10
print "the product of the digits:" ,c 

      