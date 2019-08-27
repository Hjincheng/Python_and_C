class student() :
    name = "jincheng"
    age = 24
    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def do_homework(self) :
        print('homework')

#student1 = student()
student1 = student('shuaige ',20)

print(student1.age)