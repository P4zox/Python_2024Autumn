class Person:
    def __init__ (self, name, age, favoriteFood):
        self.name=name
        self.age= age
        self.ff=favoriteFood

    def shout(self, content):
        print("我大喊:「{}」".format(content))

def introduce(self):
    print("我是 {} ，我今年{}歲，我最喜歡吃{}了!".format(self.name, self.age, self.ff))



person = Person("Amy", 15, "Apple")
introduce(person)
person.shout("我討厭牙醫!")


