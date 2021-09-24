class Turing(object):
    
    def calPoints(self):
        print("Turing test is not null;")
        
        
    def calPoint(self, ops= {""})-> str:
    
        arrayList = {""}
    
        for a in ops:
            if a == "C":
                arrayList.discard(arrayList.__sizeof__() - 1)
            else:
                if a == "D":
                    arrayList.add(arrayList.__getattribute__(arrayList.__sizeof__() - 1) * 2)
                else:
                    if a  == "+":
                        arrayList.add(arrayList.__getattribute__(arrayList.__sizeof__() - 1) +
                                      arrayList.__getattribute__(arrayList.__sizeof__() - 2))
                    else:
                        arrayList.add(int(a))
                        
        total = 0
        
        for number in arrayList:
            total += number
            
            print("The total is: " + total)
            return total
        
            
    