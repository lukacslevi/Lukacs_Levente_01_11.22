from data import vonatok, ido, keses
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
    print('6 - Késés módosítása')
    return input('Választás: ')

def fajlBetoltes():
    file=open(fajlnev,'r',encoding='utf-8')
    for row in file:
        darabolt=row.strip().split(';')
        vonatok.append(darabolt[0])
        ido.append(darabolt[1])
        keses.append(darabolt[2])
    file.close()
    
def vonatKiir():
    system('cls')
    print('--------SZEMÉLYVONATOK--------')
    for vonat in vonatok:
        print(f'\t{vonat}')
    input()
    
def idoKiir():
    for i in range(len(vonatok)):
        print(f'\t{i+1}. {vonatok[i]}: {ido[i]}, késés:{keses[i]} perc')
        
def kesesMod():
    for i in range(len(vonatok)):
        print(f'\t{i+1}. {vonatok[i]}: {ido[i]}, késés:{keses[i]} perc')
    index=input('Kérem adja meg a sorszámot: ')
    keses[int(index)-1]=input('Adja meg a késést percben: ')
        
def ujSzerelveny():
    system('cls')
    print('-------ÚJ EREDMÉNYEK--------')
    bekertVonat=input('Név: ')
    bekertIdo=input('Érkezés: ')
    vonatok.append(bekertVonat)
    ido.append(bekertIdo)
    keses.append('0')
    input('Sikeres felvétel.')
    
def mentesFajlba():
    file=open(fajlnev,'w',encoding='utf-8')
    for i in range(len(vonatok)):
        if i>0:
            file.write('\n')
        file.write(f'{vonatok[i]};{ido[i]};{keses[i]}')
    file.close()
    
def vonatokTorlese():
    system('cls')
    print('------SZERELVÉNY TÖRLÉSE------')
    idoKiir()
    sSz=int(input('\nMelyik szerelvényt töröljük? Adja meg a sorszámát: '))
    vonatok.pop(sSz-1)
    ido.pop(sSz-1)
    keses.pop(sSz-1)
    mentesFajlba()
    input('Sikeres törlés.')
