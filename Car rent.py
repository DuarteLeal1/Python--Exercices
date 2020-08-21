d = int(input('How many days was the car used? '))
km = float(input('How many kilometers did the car travel? '))
ppd = d * 60
ppkm = km * 0.15
pf = d + km
print('The final price to pay is {:.2f}'.format(pf))
