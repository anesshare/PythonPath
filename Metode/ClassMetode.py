class Student:
    count = 0
    total = 0
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count+=1
        Student.total += gpa
    #INSTANCE METHOD    
    def getInfo(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def getCount(cls):
        return f"Total number of students is : {cls.count}"     #Kod  klas metoda umesto self koristimo cls i ona moze da uzme metode i varijable iz klase
    @classmethod
    def getAvg(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total / cls.count}"

std1 = Student("Anes",3.5)
std1 = Student("Anes",10)
print(Student.getCount())
print(Student.getAvg())