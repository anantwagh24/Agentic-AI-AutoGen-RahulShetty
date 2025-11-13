class ThisKeywordExample:
    def __init__(self):
        self.a = 4  # instance variable

    def abc(self):
        a = 2  # local variable
        print("print:", a)        # prints local variable
        print("print:", self.a)   # prints instance variable (like 'this.a' in Java)


# main equivalent
obj = ThisKeywordExample()
obj.abc()
