tomeg:int = int(input('hány Kg vagy? '))
magassag:float = float(input('hány cm magas vagy? ')) / 100
tti:float = tomeg / (magassag ** 2)
print(f'TTI = {round(tti, 2)}')
print('Testsúlyosztályod:', end=' ')

if   tti < 16:   print('súlyos soványság')
elif tti < 17:   print('mérsékelt soványság')
elif tti < 18.5: print('enyhe soványság')
elif tti < 25:   print('normális testsúly')
elif tti < 30:   print('túlsúlyos')
elif tti < 35:   print('I. fokú elhízás')
elif tti < 40:   print('II. fokú elhízás')
else:            print('III. fokú (súlyos) elhízás ')