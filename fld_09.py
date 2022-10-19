fogy:float = float(input('mennyit eszik az autó 100 Km-en? '))
ar:int = int(input('mennyibe kerül a benzin? '))
ut:int = int(input('hány Km-t akarsz utazni? '))

print(f'az útiköltség {round(ar * fogy * ut / 100)} Ft')