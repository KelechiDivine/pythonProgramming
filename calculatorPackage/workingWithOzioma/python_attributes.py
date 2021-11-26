class sample:
    def __init__(self, *args):
        if len(args) > 1:
            self.ans = 0

            for index in args:
                self.ans += 1

        elif isinstance(args[0], int):
            self.ans = args[0] * args[0]

        elif isinstance(args[0], str):
            self.ans = "Hello! " + args[0]


sample_one = sample(1, 2, 3, 4, 5)
print("Sum of list : ", sample_one.ans)

sample_two = sample(5)
print("Square of int : ", sample_two.ans)

sample_three = sample("Okoroafor Kelechi Divine")
print("String : ", sample_three.ans)
