import datetime

def gettime():
    return datetime.datetime.now()






def addinfo(ch2):
    if ch2 == 1 :
        print("Anshika's information")
        print("1. for food\n")
        print("2. for exercise")
        p=int(input())
        f = open ("ad.txt","a")
        fe = open ("ae.txt","a")
        time=str([str(gettime())])

        if p == 1 :
            
            diet = input ("enter diet : ")
            f.write(time + ":" + diet + " \n")
            
        else :
            exercise = input("enter exercise : ")
            fe.write(time + ":" + exercise + "\n")
        print("successfully updated your information\n")
        f.close()
        fe.close()
        
    elif ch2 == 2 :
        print("Rohini's information")
        print("1. for food\n")
        print("2. for exercise")
        p=int(input())
        f = open ("rd.txt","a")
        fe = open ("re.txt","a")
        time=str([str(gettime())])

        if p == 1 :
            
            diet = input ("enter diet : ")
            f.write(time + ":" + diet + " \n")
            
        else :
            exercise = input("enter exercise : ")
            fe.write(time + ":" + exercise + "\n")
        print("successfully updated your information\n")
        f.close()
        fe.close()
        
    elif ch2 == 3 :
        print("Vibhushi's information")
        print("1. for food\n")
        print("2. for exercise")
        p=int(input())
        f = open ("vd.txt","a")
        fe = open ("ve.txt","a")
        time=str([str(gettime())])

        if p == 1 :
            
            diet = input ("enter diet : ")
            f.write(time + ":" + diet + " \n")
            
        else :
            exercise = input("enter exercise : ")
            fe.write(time + ":" + exercise + "\n")
        print("successfully updated your information\n")
        f.close()
        fe.close()
        
def retinfo(ch2):
    if ch2 == 1 :
        print("Anshika's information")
        print("1. for food\n")
        print("2. for exercise")
        p=int(input())
        f = open ("ad.txt","r")
        fe = open ("ae.txt","r")
        time=str([str(gettime())])

        if p == 1 :
            
            
            #f.readlines()
            for i in f :
                print(i,end="")
            
        else :
            
            #fe.readlines()
            for i in fe :
                print(i,end="")
        
        f.close()
        fe.close()
        
    elif ch2 == 2 :
        print("Rohini's information")
        print("1. for food\n")
        print("2. for exercise")
        p=int(input())
        f = open ("rd.txt","r")
        fe = open ("re.txt","r")
        time=str([str(gettime())])

        if p == 1 :
            
            
            #f.readlines()
            for i in f :
                print(i,end="")
            
        else :
            
            #fe.readlines()
            for i in fe :
                print(i,end="")
        
        f.close()
        fe.close()
        
    elif ch2 == 3 :
        print("Vibhushi's information")
        print("1. for food\n")
        print("2. for exercise")
        p=int(input())
        f = open ("vd.txt","r")
        fe = open ("ve.txt","r")
        time=str([str(gettime())])

        if p == 1 :
            
            
            #f.readlines()
            for i in f :
                print(i,end="")
            
        else :
            
            #fe.readlines()
            for i in fe :
                print(i,end="")
        
        f.close()
        fe.close()
        


ch=5
while(ch!=0):
    print("1. Enter 1 for add some information\n")
    print("2. Enter 2 for retrieve some information\n")
    print("3. Enter 0 for exit")
    ch=int(input())
    if ch== 0 : continue
    print("Choose person :\n")
    print(" 1 . Enter 1 for Anshika\n")
    print(" 2 . Enter 2 for Rohini\n")
    print(" 3 . Enter 3 for Vibhushi\n")
    ch2=int(input())
    if ch==1:
        addinfo(ch2)
    elif ch==2:
        retinfo(ch2)
    
    print("press 5 for continue\n")
    print("press 0 for stop\n")
    ch=int(input())
    
          
    
    
