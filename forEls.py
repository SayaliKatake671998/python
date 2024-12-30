pin=1234

for i in range(3):
    p=int(input("Enter the pin"))
    if(p==pin):
        print("correct pin")
        print("Transactoin successfull")
        break
    else:
        print("Incorrect pin")
else:
    print("card blocked")
    


     
   
