class staff:
    def data(self,name,code):
        self.name=name
        self.code=code
    
class teacher(staff):
    def get_data(self,subject,publication):
        self.subject=subject
        self.publication=publication
    def display(self):
        print("The name:",self.name)
        print("The code:",self.code)
        print("The subject:",self.subject)
        print("The Publication",self.publication)
class typist(staff):
    def get_data_typ(self,speed):
        self.speed=speed
    def display_typ(self):
        print("The name:",self.name)
        print("The code:",self.code)
        print("The speed:",self.speed)
class officer(staff):
     def get_data_off(self,grade):
         self.grade=grade
     def display_off(self):
        print("The name:",self.name)
        print("The code:",self.code)
        print("The grade:",self.grade)
class regular(typist):
    def get_data_reg(self,salary):
        self.salary=salary
    def display_reg(self):
        print("The name:",self.name)
        print("The code:",self.code)
        print("The code:",self.speed)
        print("The salary is:",self.salary)
class casual(typist):
    def get_data_cas(self,wages):
        self.wages=wages
    def display_cas(self):
        print("The name:",self.name)
        print("The code:",self.code)
        print("The code:",self.speed)
        print("The wages is:",self.wages)
while True:
    print("1.Teacher")
    print("2.Regular typist")
    print("3.Officer")
    print("4.Casual typist")
    print("5.Exit")
    ch=int(input("Enter your choice:"))
    if (ch==1):
        n=input("Enter the value of name:")
        c=int(input("Enter the value of code:"))
        s=input("Enter the value for Subject:")
        p=input("Enter the value for Publication:")
        teach=teacher()
        teach.data(n,c)
        teach.get_data(s,p)
        teach.display()
    elif (ch==2):
        n=input("Enter the value of name:")
        c=int(input("Enter the value of code:"))
        s=input("Enter the value for speed:")
        sal=float(input("Enter the value for salary:"))
        typ=regular()
        typ.data(n,c)
        typ.get_data_typ(s)
        typ.get_data_reg(sal)
        typ.display_reg()
    elif (ch==3):
        n=input("Enter the value of name:")
        c=int(input("Enter the value of code:"))
        g=input("Enter the value for grade:")
        off=officer()
        off.data(n,c)
        off.get_data_off(g)
        off.display_off()
    elif (ch==4):
        n=input("Enter the value of name:")
        c=int(input("Enter the value of code:"))
        s=input("Enter the value for speed:")
        w=float(input("Enter the value of wages:"))
        ctype=casual()
        ctype.data(n,c)
        ctype.get_data_typ(s)
        ctype.get_data_cas(w)
        ctype.display_cas()
    elif (ch==5):
        break
        
        
    













        
