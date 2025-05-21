class Employee:
    def __init__(self,PHourlyPay:float,PEmployeeNumber:str,PJobTitle:str):
        #DEFINE HourlyPay : REAL
        #DEFINE Jobtitle,EmployeeNumber : STRING
        #DEFINE PayYear 2022 : ARRAY(0,51) of REAL
        self.__HourlyPay=PHourlyPay
        self.__EmployeeNumber=PEmployeeNumber
        self.__Jobtitle=PJobTitle
        self.__PayYear2022=[0 for n in range(0,51)]
    
    def GetEmployeeNumber(self):
        return self.__EmployeeNumber
    
    def SetPay(self,PWeekNumber,PHours):
        self.__PayYear2022[PWeekNumber]=PHours*self.__HourlyPay
    
    def GetTotalPay(self):
        #DEFINE sum : INTEGER
        for n in self.__PayYear2022:
            sum+=n
        return sum
    
class Manager(Employee):
    def __init__(self,PHourlyPay:float,PEmployeeNumber:str,PJobTitle:str,PBonusValue:float):
        #DEFINE BonusValue : REAL
        super().__init__(PHourlyPay, PEmployeeNumber, PJobTitle)
        self.__BonusValue=PBonusValue

    def SetPay(self,PWeekNumber,PHours):
        super().SetPay(PWeekNumber,PHours*self.__BonusValue)

def EnterHours():
    #DEFINE HourlyPay : float
    #DEFINE EmployeeNumber : INTEGER
    #DEFINE count : INTEGER
    file=open("HoursWeek1.txt","r")
    global EmployeeArray
    try:
        while not EOFError:
            count=0
            EmployeeNumber=file.readline()
            HourlyPay=file.readline()
            while EmployeeNumber!=EmployeeArray[count].GetEmployeeNumber:
                count+=1
            EmployeeArray[count].SetPay(1,HourlyPay)

    except IOError:
        print("file not real")
    

#MAIN
#DEFINE EmployeeArray : ARRAY(0,8) of Employee
EmployeeArray=[Employee(0,"","") for n in range(0,8)]



try:
    file=open("Employees.txt","r")
    #DEFINE HourlyPay : float
    #DEFINE EmployeeNumber : INTEGER
    #DEFINE BonusValue : REAL
    #DEFINE JobTitle
    #DEFINE count : INTEGER
    count=0
    while not EOFError:
        HourlyPay=file.readline()
        EmployeeNumber=file.readline()
        JobTitle=file.readline()
        if not(JobTitle.isnumeric()):
            BonusValue=JobTitle
            JobTitle=file.readline()
            EmployeeArray[count]=Manager(HourlyPay,EmployeeNumber,JobTitle,BonusValue)
        else:
            EmployeeArray[count]=Employee(HourlyPay,EmployeeNumber,JobTitle)

except IOError:
    print("file is not real")

EnterHours()
for n in EmployeeArray:
    print("EmployeeNumber=",n.GetEmployeeNumber(),"total pay:",n.GetTotalPay())