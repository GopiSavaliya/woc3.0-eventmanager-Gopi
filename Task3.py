"""contact = [7624033679, 9898599700]
diary = [{
    "Name": "Gopi",
    "Contact Number": contact
    },
    {
    ""
    }
    ]

print(diary)"""

ch = 0
diary = {}

while ch == 0:
    print("\n********** Welcome To Contact Keeper **********")
    print("\n1. Add Record.")
    print("2. Record Retrieval")
    print("3. Display All Records")
    ch1 = int(input("Enter Your Choice: "))

    if ch1 == 1:
        Name = input("\nEnter Name: ")
        choice = 0
        Contacts = []
        while choice == 0:
            Contacts.append(input("Enter Contact Number: "))
            choice = int(input("Do You want to insert more Contact Numbers?(Press 0 for Yes & 1 for No): "))

        diary[Name] = Contacts

    elif ch1 == 2:
        if diary:
            Name = input("Enter Name You want to Search: ")
            flag = 0
            for i in sorted(diary.keys()):
                if i == Name:
                    print(Name)
                    print(diary[Name])
                    flag=1
            if flag == 0:
                print("Name is not found")

        else:
            print("\nNo Records Available")

    elif ch1 == 3:
        if diary:
            for i in sorted(diary.keys()):
                print(i)
                print(diary[i])
        else:
            print("\nNo Records Available")

    else:
        print("\nWrong Input...")

    ch = int(input("\nDo You want to continue?:(Press 0 for Yes & 1 for No): "))
