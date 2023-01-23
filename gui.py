from __future__ import print_function, unicode_literals
from pyfiglet import Figlet
import os
#rendered ascii text
f = Figlet(font='slant')
print (f.renderText('parasite automatization'))

#style


#apps menu
menu_options = {
    1: 'Lq bot',
    2: '',
    3: '',
    4: '',
    5: '',
    6: '',
    7: '',
    8: '',
    9: '',
    0: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '▪', menu_options[key] )

def option1():
    os.startfile(r'C:\Users\sh0cky\Desktop\Desktop\PROJEKTY\sh0cky automatization\bot\sh0cky lq bot\sh0cky automatization lq bot.bat')
     #print('Handle option \'Option 1\'')
     #f = open(r"C:\Users\sh0cky\Desktop\Bot\bot\sh0cky lq bot\sh0cky automatization lq bot.bat", 'a')
     #print(f('Running program...'))

def option2():
     os.startfile(r'C:\Users\sh0cky\Desktop\Desktop\PROJEKTY\sh0cky automatization\bot\sh0cky alexa\bocik.bat')


def option3():
     print('Handle option \'Option 3\'')


def option4():
     print('Handle option \'Option 4\'')

def option5():
     print('Handle option \'Option 5\'')

def option6():
     print('Handle option \'Option 6\'')

def option7():
     print('Handle option \'Option 7\'')

def option8():
     print('Handle option \'Option 8\'')

def option9():
     print('Handle option \'Option 9\'')


if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            option5()
        elif option == 6:
            option6()
        elif option == 7:
            option7()
        elif option == 8:
            option8()
        elif option == 9:
            option9()
        elif option == 0:
            print('Exiting...')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')