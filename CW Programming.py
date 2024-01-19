import random

Continue="Yes"
while(Continue=="Yes"):


    Name=str(input("Enter student name:"))
    print("               ""!!!!Hi",Name,"Welcome to GameInt!!!!")
    print("                                                     ")
    print("     ""***Color mapping=> 1=White,2=Blue,3=Red,4=Yellow,5=Green,6=Purple***")
    print("                                                     ")
    print("        ""**Following thinks are the game details**")
    print("                                                     ")
    print("      **You can enter only 1 to 6 numbers to the Guess Numbers**")
    print("                                                     ")
    print("    ""**If you want to exit this game type 0 0 0 0 to guess numbers**")
    print("                                                     ")
    print("           ""**You have 8 attempts in this game**")

    num1=random.randrange(1,6)
    num2=random.randrange(1,6)
    num3=random.randrange(1,6)
    num4=random.randrange(1,6)

    R1=[0,0,0,0,0,0,0,0]
    R2=[0,0,0,0,0,0,0,0]
    R3=[0,0,0,0,0,0,0,0]
    R4=[0,0,0,0,0,0,0,0]

    Guess1=0
    Guess2=0
    Guess3=0
    Guess4=0
    i=0
    Attempt_No=1
    while(Attempt_No<=8) and(Guess1!=num1 or Guess2!=num2 or Guess3!=num3 or Guess4!=num4):
        print("Attempt No:-",Attempt_No)
        Guess1=int(input("Enter your Guess1= "))
        if(Guess1>6):
            print("Please enter 1 to 6 number")
            break
        if(Guess1==num1):
            R1[i]=1
        elif(Guess1==num2 or Guess1==num3 or Guess1==num4):
            R1[i]=0
        else:
            R1[i]=None

        Guess2=int(input("Enter your Guess2= "))
        if(Guess2>6):
            print("Please enter 1 to 6 number")
            break
        
        if(Guess2==num2):
            R2[i]=1
        elif(Guess1==num1 or Guess2==num3 or Guess2==num4):
            R2[i]=0
        else:
            R2[i]=None

        Guess3=int(input("Enter your Guess3= "))
        if(Guess3>6):
            print("Please enter 1 to 6 number")
            break

        if(Guess3==num3):
            R3[i]=1
        elif(Guess3==num1 or Guess3==num2 or Guess3==num4):
            R3[i]=0
        else:
            R3[i]=None

        Guess4=int(input("Enter your Guess4= "))
        if(Guess4>6):
            print("Please enter 1 to 6 number")
            break

        if(Guess4==num4):
            R4[i]=1
        elif(Guess4==num1 or Guess4==num2 or Guess4==num3):
            R4[i]=0
        else:
            R4[i]=None
        print("Attempt               Guess               Result")
        print("____________________________________________________________")
        print(str(Attempt_No)+"                     "+ str(Guess1)+  str(Guess2)+ str(Guess3)+ str(Guess4)+ "                "+str(R1[i])+str(R2[i])+str(R3[i])+str(R4[i]))
        Attempt_No+=1
        
        if(Guess1==0 and Guess2==0 and Guess3==0 and Guess4==0):
            break

        i=i+1

    if(Guess1==num1 and Guess2==num2 and Guess3==num3 and Guess4==num4):
        print("Congratulations!!!You have won the game....")
    else:
        print("Try again...")

    print("You have scored "+str(sum(filter(None,(R1)))+sum(filter(None,(R2)))+sum(filter(None,(R3)))+sum(filter(None,(R4)))))
    Continue=str(input("Do you want to play another game(Yes/No)?"))
    if(Continue!="Yes"):
        print("        ""***Thank You***")
    





        
        

