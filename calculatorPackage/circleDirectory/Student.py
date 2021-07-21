class Student(object):
    def __init__(self, first, last, age):
        self.__name = first
        self.__lastName = last
        self.__age =age
        
    def getName(self):
        return self.__name
    

def main():
    aStudent =Student("Kelechi", "Johnson", 19)
    nm = aStudent.getName()
    print(nm)