import abc
# I do not know how to do
class Sport(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def play(self):
        pass

class Basketball(Sport):
    def play(self):
        print("Playing basketball takes 2 hours")

class Baseball(Sport):
    def play(self):
        print("Playing baseball takes 4 hours")

basketball = Basketball()
baseball = Baseball()
basketball.play()
baseball.play()
