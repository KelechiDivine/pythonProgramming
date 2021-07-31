in_one, in_two = input("Enter a two number: ").split()

def two_sum(number, target)-> list[int]:

# def two_sum(number, target):
#     number= list[int]
#     target= int
    
    for index in range(len(number)):
        for second_index in range(index + 1, len(number)):
            if number[index] + number[second_index] == target:
                return index + second_index
            

    