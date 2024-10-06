class Person:
    def __init__(self, eye, hair, workhr):
        self.eye=eye
        self.hair=hair
        self.workhr= workhr
    
    @classmethod
    def american(cls):
        return cls("blue","brown",0)
    
    @classmethod
    def taiwanese(cls):
        return cls("black", "black",0)
    
    @staticmethod
    def work(workhr):
        print("Working hours: ", workhr)
    
    def introduce(self):
        print("My eyes is {} and my hair is {}".format(self.eye, self.hair))
    
Taiwan= Person.taiwanese()
America= Person.american()
America.introduce()
Taiwan.introduce()
Person.work(8)
