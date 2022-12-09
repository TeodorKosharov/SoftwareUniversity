from Exercise.Zoo.project.mammal import Mammal
from Exercise.Zoo.project.lizard import Lizard

# Test code:

mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)
