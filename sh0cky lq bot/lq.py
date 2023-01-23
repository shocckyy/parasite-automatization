from pyfiglet import Figlet
import sys 
from datetime import date 
#GUI
f = Figlet(font='slant')
print (f.renderText('parasite automatization lq price calculation'))
#sh0cky lq
ilość = int(input('Podaj ilość(w sztukach), aby obliczyć bilans cenowy: '))
cena = int(input('Podaj cenę(od sztuki), aby obliczyć bilans cenowy: '))
#data = int(input('Podaj date(DD/MM/RRRR): '))
#print("Data:", data)
today = date.today()
print("Ilość: ", ilość)
#cena = 7
koszty = 3
ckoszty = ilość * koszty
ckwota = ilość * cena
zysk =  ckwota - ckoszty
podział = zysk / 2
print("Cała kwota:", ckwota, "zł")
print("Koszty:", ckoszty, "zł")
print("Zysk:", zysk, "zł")
print("Podział:", podział, "zł")
input("Plik został zapisany, aby wyjśc naciśnij [ENTER].")
    
with open("results.txt", "a") as text_file:
    sys.stdout = text_file
    print("--------------------------------")
    print("Data:", today)
    print("Ilość: ", ilość)
    print("Cała kwota:", ckwota, "zł")
    print("Koszty:", ckoszty, "zł")
    print("Zysk:", zysk, "zł")
    print("Podział:", podział, "zł")
    #print("--------------------------------")
sys.exit()
#MADE BY SH0CKY