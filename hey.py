# # school = ["you", "me", "us"]
# # print(school)
# # for i in school:
# #  if i == "me":
# #   continue
# #  print(i)

# # for x in range(1500, 3000):
# #  print(x)
# #  # if x == 2000:
# #   # break
# # else:
# #   print("it is finished ndien")

# x = 10

# while x < 20:
#  print(x)
#  x += 5

# def my(fname, *args):
#  print(f"afo {fname}")
#  for name in args:
#   print(f"hy {name}")
# my("mike", "joy", "ima")

# class car:
#  def __init__(self, hp, model, brand, year):
#   self.horsepower = hp
#   self.model = model
#   self.brand = brand
#   self.year = year

#  def info(self):
#   return f'{self.brand} {self.model} {self.year}'

# car1 = car(856, "motor", "toyota", 2020 )
# print(car1.info())



class Person:
 def __init__(self, name, dob):
  self.name = name
  self.dob = dob

 def __str__(self):
  return f"{self.name} was born on {self.dob}"

person1 = Person("mike", 60)
print(person1)



class Family:
 def __init__(self, fborn, sborn, tborn):
  self.fborn = fborn
  self.sborn = sborn
  self.tborn = tborn

 def __str__(self):
  return f"{self.fborn} is a good man. i don't like {self.sborn} but {self.tborn} is also good"
family1 = Family("mike", "joe", "gabs")

print(family1)























try:
 print(x)
except Exception as err:
 print(err)
else:
 print("success")
finally:
 print("the try except is finished")

raise Exception("oops try again bro")






class Gfarmily(Family):
 def __init__(self, fborn, sborn, tborn, gname):
  super().__init__(fborn, sborn, tborn)
  self.gname = gname

 def __str__(self):
  return f"their group name is now {self.gname}"

 def is_older(self):
  return True if self.gname > 60 else False

Gfarmily1 = Gfarmily("mike","joe","gabs", 70 )
print(Gfarmily1)
print(Gfarmily1.is_older())



