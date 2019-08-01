#Program to get input from user as a list  containing name, age, rollno, adharno
#And then search the list  by rollno, adharno
StuList = [];#An empty list
def Get_StudentDetails(StuList) :
    Ch = 'Y';  # In order to continue adding student details or not , we need this variable
    while Ch == 'Y' or Ch == 'Yes':
        Name = input("Enter Name of the student : ")
        Age = input("Enter Age :")
        RollNo = input("Enter RollNo : ")
        AdharNo = input("Enter AdharNo : ")
        StuTuple = (Name,Age,RollNo,AdharNo)
        StuList.append(StuTuple)
        Ch = input("Add more students <y/n> : ").upper();
        if Ch == 'N' or Ch == 'No':
            break
#Print student details
def Print_StuDetails() :
    print()
    print("Student Details List..")
    print()
    print("-" * 70)
    print("{0:12}{1:>15}{2:>15}{3:>15}".format("StudentName","Age","RollNo","AdharNo"))
    print("-" * 70)
    for StuTuple in StuList:
        Name,Age,RollNo,AdharNo = StuTuple                                          
        print("{0:12}{1:>20}{2:>20}{3:>20}".format(Name,Age,RollNo,AdharNo))
    print("-" * 70)
#Search Student Details by RollNo
def Search_By_RollNoOrAdhar(SearchOptions,SearchValue) :
    Flag = 0
    StuName = ""
    Roll_No = ""
    Adhar_No = ""
    StuAge = ""
    for StuDetails in StuList:
        Name,Age,RollNo,AdharNo = StuDetails
        if (SearchOptions == 1) :
            if (SearchValue == RollNo) :
                print("Searching By RollNo..")
                Flag = 1
                StuName = Name
                StuAge = Age
                Roll_No = RollNo
                Adhar_No = AdharNo
                break
        if (SearchOptions == 2) :
            if (SearchValue == AdharNo) :
                print("Searching By AdharNo..")
                Flag = 1
                StuName = Name
                StuAge = Age
                Roll_No = RollNo
                Adhar_No = AdharNo
                break
    if (Flag == 1) :
        print("Student Name",StuName)
        print("Student Age",StuAge)
        print("RollNo",Roll_No)        
        print("Student Adhar No",Adhar_No)
            
    if (Flag == 0) :
        print("Searched RollNo/AdharNo %s is not present in Student List" %SearchValue)
#Appending Student Details
Get_StudentDetails(StuList)
#Print Student Details
Print_StuDetails()
Search = 'y'
while  Search == 'y' :
    SearchOptions = int(input("Enter 1 for Search by RollNo or 2 for Search by AdharNo :"))
    SearchValue = "";
    if (SearchOptions == 1) :
        SearchValue = input("Enter the RollNo to search in student list..")
    elif (SearchOptions == 2) :
        SearchValue = input("Enter the AdharNo to search in student list..")
    else :
        print("Invalid options given")
#Search By RollNoOrAdhar

    Search_By_RollNoOrAdhar(SearchOptions,SearchValue)
    Search = input("Search Again <y/n> : ").lower();
    if Search == 'N' or Search == 'No':
        break

      
