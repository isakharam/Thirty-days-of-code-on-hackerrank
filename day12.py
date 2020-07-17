lass Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)
class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores=scores    
    def calculate(self):
        j=0
        length=len(self.scores)
        for i in self.scores:
            j+=i
        avg_marks=int(j/length)
        if(avg_marks>=90 and avg_marks<=100):
            return("O")
        elif(avg_marks>=80 and avg_marks<=90):
            return("E")
        elif(avg_marks>=70 and avg_marks<=80):
            return("A")
        elif(avg_marks>55 and avg_marks<=75):
            return("P")
        elif(avg_marks>=40 and avg_marks<=55):
            return("D")
        elif(avg_marks<40):
            return("T")
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())    
