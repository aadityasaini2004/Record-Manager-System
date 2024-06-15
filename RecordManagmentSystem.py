import pickle

def add_Records():
    r = int(input("How many record's you want to enter "))
    for i in range(r):
        id=int(input("Enter Student_id "))
        name=input("Enter Student_name ")
        marks=int(input("Enter Student_marks "))
        rec=[id,name,marks]
        f=open("Student.dat",'ab')
        pickle.dump(rec,f)
        f.close()

def readRecords():
    f=open("Student.dat",'rb')
    while True:
        try:
            rec=pickle.load(f)
            for i in rec:
                print(i,end=" ")
            print()
        except EOFError:
            break
    f.close()

def searchRecords():
    f=open("Student.dat",'rb')
    r=int(input("Enter Student_id to search "))
    flag = False
    while True:
        try:
            rec=pickle.load(f)
            if rec[0]==r:
                print("Record's Found--> " ,rec)
                flag=True
        except EOFError:
            break
    if flag == False:
        print("No Record's Found!")
    f.close()

def updateRecords():
    f=open("Student.dat",'rb')
    r=int(input("Enter Student_id to update "))
    temp=[]
    flag = False
    while True:
        try:
            rec=pickle.load(f)
            temp.append(rec)
            flag = True
        except EOFError:
            break
    f.close()
    for i in temp:
        if i[0]==r:
            new_Marks = int(input("Enter new marks "))
            i[2] = new_Marks
    f=open("Student.dat",'wb')
    for i in temp:
        pickle.dump(i,f)
    if flag == False:
        print("No Record's Found!")
    f.close()

def deleteRecords():
    f=open("Student.dat",'rb')
    r=int(input("Enter Student_id to update "))
    temp=[]
    flag = False
    while True:
        try:
            rec=pickle.load(f)
            temp.append(rec)
            flag = True
        except EOFError:
            break
    f.close()
    f=open("Student.dat",'wb')
    for i in temp:
        if i[0]==r:
            continue
        else:
            pickle.dump(i,f)
    if flag == False:
        print("No Record's Found!")
    f.close()

while True:
    print("Main_Menu")
    print("1. Add_Records")
    print("2. Display_Records")
    print("3. Search_Records")
    print("4. Update_Records")
    print("5. Delete_Records")
    print("6. Exit")
    choice = int(input("Enter your choice..? "))
    if choice == 1:
        add_Records()
    elif choice == 2:
        readRecords()
    elif choice == 3:
        searchRecords()
    elif choice == 4:
        updateRecords()
    elif choice == 5:
        deleteRecords()
    elif choice == 6:
        print("Good Bye!")
        exit()
    else:
        print("Enter Valid choice!")