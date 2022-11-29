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
    print('4 - Szerelvények mentése fájlba')
    print('5 - Szerelvény törlése a menetrendből')
    return input('Választás: ')

def fajlBetoltes():
    file=open(fajlnev,'r',encoding='utf-8')
    for row in file:
        darabolt=row.strip().split(';')
        vonatok.append(darabolt[0])
        ido.append(darabolt[1])
    file.close()
    
def vonatKiir():
    system('cls')
    print('--------SZEMÉLYVONATOK--------')
    for vonat in vonatok:
        print(f'\t{vonat}')
    input()
    
def idoKiir():
    for i in range(len(vonatok)):
        print(f'\t{i+1}. {vonatok[i]}: {ido[i]}')
        
def ujSzerelveny():
    system('cls')
    print('-------ÚJ EREDMÉNYEK--------')
    bekertVonat=input('Név: ')
    bekertIdo=input('Érkezés: ')
    vonatok.append(bekertVonat)
    ido.append(bekertIdo)
    input('Sikeres felvétel.')
    
def mentesFajlba():
    file=open(fajlnev,'w',encoding='utf-8')
    for i in range(len(vonatok)):
        if i>0:
            file.write('\n')
        file.write(f'{vonatok[i]};{ido[i]}')
    file.close()
    
def vonatokTorlese():
    system('cls')
    print('------SZERELVÉNY TÖRLÉSE------')
    idoKiir()
    sSz=int(input('\nMelyik szerelvényt töröljük? Adja meg a sorszámát:'))
    vonatok.pop(sSz-1)
    ido.pop(sSz-1)
    mentesFajlba()
    input('Sikeres törlés.')
