class Turing(object):
    
    def calPoints(self):
        print("Turing test is not null;")
    
    def calPoint(self, ops):
        
        arrayList = []
        
        for a in ops:
            if a == "C":
                arrayList.remove(arrayList[len(arrayList) - 1])
            else:
                if a == "D":
                    arrayList.append(arrayList[len(arrayList) - 1] * 2)
                else:
                    if a == "+":
                        arrayList.append(arrayList[len(arrayList) - 1] +
                                         arrayList[len(arrayList) - 2])
                    else:
                        (arrayList.append(int(a)))
        
        total = 0
        
        for number in arrayList:
            total += number
        print(f"The total is: {total}")
        return total
    