class Monkey:

    Greeting = ""
    
    def __init__(self, Name="there"):
        self.Greeting = Name + "!"
    
    def SayHello(self):
        print("Hello {0}".format(self.Greeting))
