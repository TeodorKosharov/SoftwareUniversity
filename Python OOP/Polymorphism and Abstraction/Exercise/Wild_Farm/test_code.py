from Exercise.Wild_Farm.project.animals.birds import Owl
from Exercise.Wild_Farm.project.food import Meat, Vegetable

owl = Owl("Pip", 10, 10)
print(owl.food_eaten)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)
