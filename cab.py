username="nishok"
password="1234"
i=3



while i>=0:
  print("username=")
  a=raw_input()
  print("password=")
  b=raw_input()
  if(username==a and password==b):
    

   print("login successfull")

   source=0

   print("enter destination value")

   destination=int(input())

   print("select car model \n1.micro \n2.premium \n3.luxury")

   n =int(input())

   if n==1:

     print("1.alto \n2.swift \n3.indico")

     if destination<5:

       print("price=20")

     else:

        destination=destination*4 

        print("price=",destination)

   elif n==2:

     print("1.sumo \n2.innovo \n3.xuv")

     if destination<5:

       print("price=30")

     else:

         destination=destination*6

         print("price=",destination)



   elif n==3:

     print("1.BMW \n2.Audi \n3.Benz")

     if destination<5:

       print("price=50") 

     else:

        destination=destination*8

        print "price=",destination





   print "BILL RECEIPT:"
    
   print "name=",username

   print "car type=",n

   print "price=",destination

   break

  

  

  else:
   if i>0: 
     print "given username or password is incorrect",i,"times remaining" 
     i-=1
   else:
     print "BLOCKED"
     print "entered wrong information more than 3 times"
     break
    
   