class Student:
    name = None
    age = None

    def say_hi(self):
        print(f"Hi,大家好，我是{self.name}")



stu = Student()
stu.say_hi()
stu.name="Jack"
stu.say_hi()
