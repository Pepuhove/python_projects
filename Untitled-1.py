"""
sent = "The water earth and air are vital"
acro = ""
a = sent.split()
b = [a[1], a[2], a[4], a[5],a[6]]# Removed an extra square bracket here


for word in b:
    
    acro += word[:2].upper()+(".")
    acro=acro[0:14]
    

print(acro)
"""
class Person:
    department = "Computer Science"
    def set_name(self,new_name):
        self.name=new_name
    def set_location(self,new_location):
        self.location=new_location

