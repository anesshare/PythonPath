#Metoda koja pripada vise klasi nego bilo kojem objektu klase tj instanci

class Employee:
    def __init__(self,name,job):
        self.name = name
        self.job=job
    def getInfo(self):
        return f"{self.name} {self.job}"
    
    @staticmethod
    def isValidJob(job):                                        #NE MOZES DA JE POZOVES NA OBJEKTE U OVOM SLUCAJU EMP1 VEC MOZES SAMO...
        validJobs = ["Manager","Cashier","Cook","Janitor"]
        return job in validJobs
print(Employee.isValidJob("Janitor"))                           #...OVAKO, SAMO KLASI PRIPADA
empl = Employee("Anes","Engineer")
emp2 = Employee("Canco","Manager")

print(empl.getInfo())