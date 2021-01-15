#exmaple
import random
def Password():
    a ='1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*(-=+_/|\}{[~'
    x ='!@#$%^&*(-=+_/|\}{[~'
    z ='abcdefghijklmnopqrstuvwxyz'
    
    b =int(input("enter a length: "))
    print("".join(random.sample(a,b)))
Password()


def UserNama():
    import random
    a ='0123456789'
    b =''.join(random.sample(a,10))
UserName()  


#otp generation...
l1 =[]
def OTP_GENERATON():
    import random  
    a ='0123456789'
    while True:
        length =int(input("how many number otp you wont to get: "))
        for i in range(length):
            z =random.choice(a)
            l1.append(z)
        print(' '.join(l1))
        l1.clear()
        #print(' '.join(random.sample(a,length)))               
        
        
        
#make a game.. in python..
import random
l1 =['Stone','Paper','Scissors']
attempt =5
l =" ".join(l1)
Loss_List =[]
Win_List =[]
Tie_List =[]
Att =[]
name =input("Enter your name: ")
print(f"welcome to the [{l}] Game [{name}] ")
print("\n")
print("Game ruls: ")
print(f"you have a total {attempt} attempt [{name}]... and lose points consider -20 and win point consider +10 and when your game is tye then tye points consider +10")
print("\n")
print(f"ok then Good luck and go further [{name}]")
ran =random.randint(0,2)
Computer =l1[ran]
me =1
i =0
att =5
while attempt>i:
    me =input(f"Enter your choise!!!!..from : {[l1]}")
    if Computer!=me not in l1 :
        att =att+1
        Att.append(att)
        print(f"please selected from give list: [{l1}]")
        
        
    if Computer=='Paper'and me in l1:
        if me=='Stone':
            str ="you  loss"
            Loss_List.append(str)
        elif me=='Paper':
            str ="Match tie.."
            Tie_List.append(str)
        else:
            str ="you win.."
            Win_List.append(str)
        
        
    elif Computer=='Scissors'and me in l1:
        if me =='paper':
            str ="you loss"
            Loss_List.append(str)
        elif me=='Scissors':
            str ="Match tie.."
            Tie_List.append(str)
        else:
            str ="you win..."
            Win_List.append(str)
            
            
        
    elif Computer=='Stone'and me in l1:
        if me=='Scissors'and me=='Stone':
            str ="you loss."
            Loss_List.append(str)
        elif me=='Stone':
            str ="Match tie.."  
            Tie_List.append(str)
        else:
            str ="you win"
            Win_List.append(str)
        
        
    me=1
    ran =random.randint(0,2)
    Computer =l1[ran]
    i =i+1

else:
    w =len(Loss_List)
    x =len(Win_List)
    z =len(Tie_List)
    a =len(Att)
    if a>2:
        Attp_score =-10
    else:
        Attp_score =0   
    w_point =x*20
    l_point =(w*20)
    t_point =z*10
    f_point =(w_point+t_point-l_point+Attp_score)
    print("Ok your Attempt is over..")
    print("\n")
    print("Now the time for score..")
    print(f"{name} Your Loss Point IS : {l_point}")
    print(f"{name} Your Win Point Is : {w_point}")
    print(f"{name} Your Tye Point IS : {t_point}")
    print(f"{name} Your wrong_Attempt Data:{a}")
    print("\n")
    print("Score Bord......")
    print(f"{[f_point]}")
    
    
    
#random module
import random
a =random.randint(0,10)
str ="123456789"
b =random.sample(str,4)
print(''.join(b))
l1 =[1,2,3,4,5]
c =random.choices(l1,k =2)
print(c)
d =random.random()
print(d)    
