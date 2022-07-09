name=[]
address=[]
phone=[]
room=[]
i=1
def booking():
    name.append(input("Enter Name"))
    address.append(input("Enter Address"))
    phone.append(int(input("Enter Phone Number")))
    room.append(len(room))
def Vacate():
    s=input("Enter Name To Vacate")
    for i in range(len(name)):
        if(s==name[i]):
            break
    name.remove(name[i])
    address.remove(address[i])
    phone.remove(phone[i])
    room.remove(room[i])
def Display():
    for i in range(len(room)):
        print("{} {} {} {}".format(name[i],address[i],phone[i],room[i]))
def Home():
    print("\t\t\t\t\t\t WELCOME TO HOTEL ANCASA\n")
    print("\t\t\t 1 Booking\n")
    print("\t\t\t 2 Vacate\n")
    print("\t\t\t 3 Record\n")
    print("\t\t\t 0 Exit\n")
   
ch=int(input("->"))
      
if ch == 1:
    print(" ")
    booking()
      
elif ch == 2:
    print(" ")
    Vacate()

elif ch == 3:
    print(" ")
    Display()
      
else:
    exit()

for i in range(10):
    x=int(input())
    if(x==4):
        break
    else:1
      Home()
