class Turing(object):
    
    def calPoints(self):
        print("Turing test is not null;")
        
        
    def calPoint(self, ops=[])-> str:
    
        arrayList = []
    
        for a in ops:
            if a == "C":
                arrayList.remove(arrayList.__len__() - 1)
            else:
                if a == "D":
                    arrayList.append(arrayList.index(arrayList.__len__() - 1) * 2)
                else:
                    if a  == "+":
                        arrayList.append(arrayList.index(arrayList.__len__() - 1) +
                                         arrayList.index(arrayList.__len__() - 2))
                    else:
                        arrayList.append(int(a))
                        
        total = 0
        
        for number in arrayList:
            total += number
            
            print("The total is: " + total)
            return total
        
            
    