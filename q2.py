xy = [
   ['a', 'e'],
   [1,3,7,9]
]
import itertools
for element in itertools.product(*xy):
    print(element)
