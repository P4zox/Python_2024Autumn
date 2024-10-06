import abc

# ==封裝encapsulation===============================================================================
# class Student:
#     def __init__(self, name):
#         self.__name = name
#         self.__score = {"Math":0, "Physics":0, "Chemistry":0}
#     #私有方法
#     def __add_subject(self, subject):
#         self.__score[subject]=0
#     #公有方法
#     def set_score(self, subject, score):
#         if subject not in self.__score:
#             self.__add_subject(subject)
#         self.__score[subject]=score

#     def get_subject(self):
#         for key in self.__score:
#             print("{} : {}".format(key,self.__score[key]))
    

# bob=Student("bob")
# bob.set_score("Chinese", 0)
# bob.get_subject()

# ==繼承inheritance===============================================================================
# 被繼承的類別 -> 父親別
# class Person:
#     def __init__(self,name,age,ID):
#         self.name = name
#         self.age = age
#         self.__ID = ID
#     def speak(self, sentence):
#         return self.name + " says " + sentence

# #繼承 Person 的類別 -> 子類別    
# class Athlete(Person):
#     def workout(self):
#         return "%s goes to the gym to excercise. " % (self.name)
#     #覆寫建構子
#     def __init__(self, name ,age, ID, height):
#         super().__init__(name, age , ID )
#         self.height= height
#     #覆寫 speak 方法
#     def speak(self, sentence):
#         print("Athlete: ",super().speak(sentence))

# ==多型polymothism===============================================================================
class Member(metaclass=abc.ABCMeta):
    def __init__(self, name, level):
        self.name=name
        self.level=level

    @abc.abstractmethod
    def discount(self, price):
        pass

    def buy(self,price):
        d_price=self.discount(price)
        print(self.name,"'s member level is {}. After discount: {}".format(self.level, d_price))

class GoldenMember(Member):
    def __init__(self, name, level):
        super().__init__(name, level)
        self.discount_rate = 0.9

    def discount(self, price):
        return price * self.discount_rate
    
class VIPMember(Member):
    def __init__(self, name, level):
        super().__init__(name, level)
        self.discount_rate = 0.8
    def discount(self, price):
        return price * self.discount_rate

john = GoldenMember("John", "Golden")
amy = VIPMember("Amy", "VIP")
john.buy(2000)
amy.buy(2000)