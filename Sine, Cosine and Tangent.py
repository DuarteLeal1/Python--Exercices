from math import radians, cos, sin, tan

angle = float(input('How wide is the angle? '))

cosseno = cos(radians(angle))
print('The cosine is {:.2f}'.format(cosseno))

sin = sin(radians(angle))
print('The sine is {:.2f}'.format(sin))

tangente = tan(radians(angle))
print('The tangent is {:.2f}'.format(angle))
