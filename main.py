import convet as AS
import bit_adder as LL


ContinueLoop=True
Nim1=True
Nim2=True
inf=True
while ContinueLoop==True:
    while Nim1==True:
        try:
            In_No=int(input("Enter First Number : "))  
            flag1=True
            Nim1=False
            if inf==True:
                Nim2=True
            while flag1==True:
                if In_No<256 and In_No >=0:
                    A=AS.conf(In_No)
                    flag1=False
                else:
                    print("Error Try again !!")
                    In_No=int(input("Please Enter number between 0-255 : "))
                    flag1=True
        except:
            print("Please Enter Integer (0-255)")
    while Nim2==True:
        try:
            flag2=True  
            In_No2=int(input("Enter Second Number : "))
            Nim2=False
            if inf==True:
                Nim1=True
            while flag2==True:
                if In_No2<256 and In_No2 >=0:
                    B=AS.conf(In_No2)
                    flag2=False
                else:
                    print("Error Try again !!")
                    In_No2=int(input("Please Enter number between 0-255 : "))
                    flag2=True
        except:
            print("Please Enter Integer (0-255)")
  
    F=LL.final(A,B)
    
    print("************************************************************")
    print("The binary Conversion of",In_No, "input is",A)
    print("The binary Conversion of" ,In_No2,"input is",B)
    print("The binary addition of",A, "and" ,B, "is :",F)
    print("***********************************************************") 
    Continue=input("Do you want to continue (Y/N) : ").lower()
    if Continue == "y":
        ContinueLoop=True
    else:
        print("good bye!!!")
        ContinueLoop=False
        


