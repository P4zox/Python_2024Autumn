import abc
# I do not know how to do
class Sport(metaclass=abc.ABCMeta):
    def __init__(self, sport, hr):
        self.sport=sport
        self.hr=0

    @abc.abstractmethod
    def discount(self, hr):
        pass

    def buy(self,hr):
        d_price=self.discount(hr)
        print("Playing {} takes {}hr".format(self.sport, d_price))

class Basketball(Sport):
    def __init__(self, sport, hr):
        super().__init__(sport,hr)
        self.discount_rate = 2

    def basketball(self, hr):
        return hr + self.discount_rate
    
class Baseball(Sport):
    def __init__(self, sport, hr):
        super().__init__(sport, hr)
        self.discount_rate = 4
    def discount(self, hr):
        return hr + self.discount_rate

john = Basketball("basketball", 2)
amy = Baseball("baseball",4)
john.buy(2)
amy.buy(2)