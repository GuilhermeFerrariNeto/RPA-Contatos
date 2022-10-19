import pyautogui as eu
from time import sleep

consulta = open('Cnpj.txt')
for linha in consulta:
    cnpj = linha

    eu.click(312,249,duration=0.5)
    eu.write(cnpj,interval=0.04)
    eu.click(500,324,duration=1)
    sleep(3)
     
    if eu.locateOnScreen('print de conferencia.png'):
        eu.click(866,162,duration=0.5)
        eu.click(575,750)
        eu.press('enter')
        eu.write('N')
        eu.click(516,754)
        eu.click(398,245,duration=0.5)
        eu.dragTo(247,246,duration=1,button='left')
        eu.press('delete')
        continue
    if eu.locateOnScreen('print de conferencia 3.png'):
        eu.click(575,750)
        eu.press('enter')
        eu.write('N')
        eu.click(516,754)
        eu.click(398,245,duration=0.5)
        eu.dragTo(247,246,duration=1,button='left')
        eu.press('delete')
        continue
    else:
        eu.locateOnScreen('print de conferencia 2.png')
        eu.click(1264,260,duration=0.5)
        sleep(5)
        #pegar Nome do Cliente
        eu.click(1189,297,duration=0.5)
        eu.click(1189,297)
        eu.click(1189,297)
        eu.hotkey('ctrl', 'c')
        eu.click(567,738)
        eu.press('enter')
        eu.hotkey('ctrl', 'v')
        eu.click(515,750,duration=1)
        #pegar numero Res
        eu.click(1135,354,duration=1)
        eu.click(1135,354)
        eu.click(1135,354)
        eu.hotkey('ctrl', 'c')
        eu.click(567,738)
        eu.click(1119,182,duration=0.5)
        eu.hotkey('ctrl', 'v')
        eu.click(515,750,duration=1)
        #pegar numero celular
        eu.click(511,358,duration=1)
        eu.click(511,358)
        eu.click(511,358)
        eu.hotkey('ctrl', 'c')
        eu.click(567,738,duration=1)
        eu.press('space')
        eu.hotkey('ctrl', 'v')
        eu.click(515,750,duration=1)
        #pegar numero com
        eu.click(166,409,duration=1)
        eu.click(166,409)
        eu.click(166,409)
        eu.hotkey('ctrl', 'c')
        eu.click(567,738)
        eu.press('space')
        eu.hotkey('ctrl', 'v')
        eu.click(515,750,duration=1)
        #pegar email
        eu.click(542,413,duration=1)
        eu.click(542,413)
        eu.click(542,413)
        eu.hotkey('ctrl', 'c')
        eu.click(567,738)
        eu.press('space')
        eu.hotkey('ctrl', 'v')
        eu.click(515,750,duration=1)
        #agendado retorno
        eu.click(1194,184,duration=1)
        sleep(1.5)
        eu.click(1094,203,duration=0.2)
        eu.click(510,106,duration=1)
        sleep(2)