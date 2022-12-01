from functions import *
from os import system

fajlBetoltes()

valasztas=''
while valasztas!='0':
    system('cls')
    valasztas=menu()
    if valasztas=='1':
        system('cls')
        vonatKiir()
    elif valasztas=='2':
        system('cls')
        print('----SZERELVÉNYEK KILISTÁZÁSA----')
        idoKiir()
        input()
    elif valasztas=='3':
        system('cls')
        ujSzerelveny()
    elif valasztas=='4':
        system('cls')
        mentesFajlba()
        input('Sikeres mentés...')
    elif valasztas=='5':
        system('cls')
        vonatokTorlese()  
    elif valasztas=='6':
        system('cls')
        kesesMod()  