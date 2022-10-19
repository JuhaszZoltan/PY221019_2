print('''
=====árlista=====
alma    350 Ft/Kg
körte  1180 Ft/Kg
szilva  500 Ft/Kg
=================
''')
vegosszeg:float = 0
kerdes:str = 'Jó reggelt, szeretne valamit vásárolni? '
while input(kerdes).lower() == 'igen':
    termek = input('Mit szeretne vásárolni? ')
    if termek not in ['alma', 'körte', 'szilva']:
        print(f'Sajnálom, de {termek} most nincs! :(')
    else:
        mennyiseg:float = float(input(f'Hány Kg {termek}t szeretne? '))
        if termek == 'alma':
            vegosszeg += (350 * mennyiseg)
        elif termek == 'körte':
            vegosszeg += (1180 * mennyiseg)
        elif termek == 'szilva':
            vegosszeg += (500 * mennyiseg)
    kerdes = 'Szeretne még valami mást vásárolni? '
print(f'Rendben! {round(vegosszeg)} Ft-ot szeretnék kérni!')