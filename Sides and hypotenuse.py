import math
co = float(input('What is the opposite side length? '))
ca = float(input('What is the length of the adjacent side? '))
hi = math.hypot(co, ca)
print('The length of the hypotenuse is {: .2f}'.format(hi))