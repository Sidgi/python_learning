class Myclass:
    x = 5

p1 = Myclass()

print(p1.x)

print(type(p1))


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + str(self.age))

p1 = Person("John", 36)
p1.myfunc()

