from data import vonatok, ido
from os import system
fajlnev='vonatok.csv'

def menu():
    system('cls')
    print('------------MENÜ------------')
    print('0 - Kilépés')
    print('1 - Személyvonatok')
    print('2 - Szerelvények kilistázása')
    print('3 - Új szerelvény felvétele')
    print('4 - Szerelvény törlése')
    return input('Választás: ')