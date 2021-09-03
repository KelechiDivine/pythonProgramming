

i = "welcome"


def welcome(i):
    i = i + "welcome to turing "
    return i

welcome("Developer")
print(i)


print("Welcome to TURING".capitalize())

import re
result = re.findall("Welcome to turing", "Welcome", 1)
print(result)

a = [1, 2, 3, 4]
b= [sum(a[0:x+1]) for x in range (0, len(a))]
print(b)

alphabeth = "abcd"
for i in range (len (alphabeth)):
    alphabeth[i].upper()

print(alphabeth)


class Welcome:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Welcome to ", self.name)

cw = Welcome("Turing")
cw.say_hello()


class hello :
    def __init__(self, a= "welcome to "):
        self.a = a

    def welcome(self, x):
        print(self.a+x)

h = hello()
h.welcome("Turing")


data = [10, 20,  30,  40, 50]
data.pop()
print(data)
data.pop(2)
print(data)


x =     "abcdef"
i = "a"
while i in x[:-1]:
    print(i, end= " ")

f = None
for i in range(5):
    with open ("app.log", "w") as f:
        if i > 2:
            break

print(f.closed)


def add(c,k):
    c.test = c.test +1
    k = k +1

class Plus:
    def __init__(self):
        self.test = 0

def main():
    p = Plus()
    index = 0

    for i in range (0, 25):
        add(p, index)

    print("p.test=", p.test)
    print("index", index)

main()


def func1():
    x = 50
    return x

func1()
print(x)


class Developer:
    def __init__(self):
        self.__seniority = "Junoir"
        self.skills = ""

    def display(self):
        print("Welcome to turing with {senirity} developer with skills"
              "{skills}".format(senirity = self.__seniority, skills = self.skills))

class NodeJs(Developer):
    def __init__(self):
        super().__init__()
        self.__seniority = "Senior"
        self.skills = "NodeJs"

c = NodeJs()
c.display()

Y = [2, 5J, 6]
Y.sort()
print(Y)