larg = float(input('Enter the width of the wall in meters: '))
alt = float(input('Enter the height of the wall in meters: '))
area = larg * alt
ink = area / 2
print('Your wall is {} x {} in size and your area is {:.3} m ^ 2.\n'
      'To paint the wall with paint you need {} L of paint.'.format(larg, alt, area, ink))
