from functions import menu, fajlBetoltes, vonatKiir, idoKiir, ujSzerelveny
from os import system

fajlBetoltes()

valasztas=''
while valasztas!='0':
    valasztas=menu()
    if valasztas=='1':
        vonatKiir()
    elif valasztas=='2':
        system('cls')
        print('----SZERELVÉNYEK KILISTÁZÁSA----')
        idoKiir()
        input()
    elif valasztas=='3':
        ujSzerelveny()