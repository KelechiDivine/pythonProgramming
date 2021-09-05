# class Admin:
#     def __init__(self, age, email, name, password, phoneNumber):
#         self.isName= name
#         self.isAge= age
#         self.isEmail= email
#         self.isPhoneNumber= phoneNumber
#         self.isPassword= password

class MyClass(object):
    def __init__(self, number):
        self.number = number

my_objects = []

for i in range(100):
    my_objects.append(MyClass(i))

# later

for obj in my_objects:
    print (obj.number)