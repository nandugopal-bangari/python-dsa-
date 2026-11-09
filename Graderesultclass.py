class Sresult:
    Name="Snake sai"
    Rollno=48
    MarksPhy=99
    Markscrt=99
    MarksM2=99
    def calculate(self):
        Total=self.MarksPhy+self.Markscrt+self.MarksM2
        Average=Total/3
        print(Total)
        print(Average)
        if(Total>=90):
            print("Grade A")
        elif(Total>=75):
            print("Grade B")
        elif(Total>=60):
            print("Grade c")
        elif(Total>=40):
            print("Grade D")
        else:
            print("Fail")
r=Sresult()
print(r.Name)
print(r.Rollno)
print(r.MarksPhy)
print(r.Markscrt)
print(r.MarksM2)
r.calculate()

                    
            
            
        
    
    