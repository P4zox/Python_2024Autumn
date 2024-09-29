class Person:
    def __init__(self, eye, hair):
        self.eye=eye
        self.hair=hair
    
    @classmethod
    def american(cls):
        return cls("blue","brown")
    
    @classmethod
    def taiwanese(cls):
        return cls("black", "black")
    
    def introduce(self):
        print("My eyes is {} and my hair is {}".format(self.eye, self.hair))
    
Taiwan= Person.taiwanese()
America= Person.american()
America.introduce()
Taiwan.introduce()
