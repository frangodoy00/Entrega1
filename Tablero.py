import PySimpleGUI as sg        # Importacion de los paquetes que son necesarios para la ejecucion
import json                     # del programa.
import random
import pattern.es

def verificarPalabra(palabra):                  # Esta funcion recibe un String y verifica si la palabra    
    pal=palabra.lower()                         # ingresada es correcta o no.
    ok=False
    if pal in pattern.es.lexicon:
        if pal in pattern.es.spelling:
            ok=True
    return ok

def sumar(palabra,DicSumador,Bolsa):                # Esta funcion recibe la palabra correcta para sumar los puntos,
    puntos=0                                        # un diccionario (DicSumador) que obtiene coordenadas y el color de
    o=0                                             # dicha coordenada y otro diccionario (Bolsa), que contiene el puntaje de
    aux=0                                           # cada letra. La funcion devuelve los puntos totales que el jugador
    aux2=0                                          # o la cpu obtuvo en la jugada.
    x=list(DicSumador)
    for i in palabra:
        if(DicSumador[x[o]]=='yellow'):
            puntos=puntos+(int(Bolsa[i][1])*2)
        elif(DicSumador[x[o]]=='green'):
            puntos=puntos+int(Bolsa[i][1])
            aux=aux+1
        elif(DicSumador[x[o]]=='red'):
            puntos=puntos+int(Bolsa[i][1])
            aux2=aux2+1    
        else:
            puntos=puntos+int(Bolsa[i][1])
        o=o+1
    if aux>0:
        for i in range(aux):   
            puntos=puntos*2
    if aux2>0:
        for i in range(aux2):
            puntos=puntos-2
    return(puntos)                

def cancelarPalabra(TableroDigital,DicSumador,FormarPalabra,letra_act):             # Esta funcion recibe una matriz (no visible al usuario), un diccionario,
    x=DicSumador.keys()                                                             # y dos Strings, todos para actualizarlos debido a que se tiene que cancelar
    c=0                                                                             # la jugada. Se retorna el String donde se estaba formando la palabra, ya que
    for i in x:                                                                     # los Strings no se modifican en funciones como las otras estructuras.
        TableroDigital[i[0]][i[1]]=('null')
    for i in DicSumador:
        windowT[i[0],i[1]].update('',button_color=('white',DicSumador[i]))
    if(letra_act!=''):
        FormarPalabra=FormarPalabra+letra_act
    for i in range(0,7):
        if(windowT[i].GetText()==''):
            windowT[i].update(FormarPalabra[c], button_color=('white','black')) 
            c=c+1
    DicSumador={}
    FormarPalabra=''
    return FormarPalabra

def cambiarAUX(valores,letras,Bolsa):                   # Esta funcion es un metodo auxiliar que ayuda la funcionalidad
    for valor in valores:                               # de la funcion siguiente.
        o=repartir(Bolsa)
        indice = letras.index(valor)
        letras[indice]=o
        Bolsa[valor][0]=int(Bolsa[valor][0])+1
    return letras

def CambiarFichas(Bolsa, vector):                                                                               # Esta funcion recibe el diccionario (Bolsa) para reponer las fichas
    letras=vector                                                                                               # que se desean cambiar y reartir la misma cantidad de fichas que se
    sg.theme('Light Yellow')                                                                                    # cambiaron. Quedando asi en el vector que se recibe las fichas nuevas.
    layout = [[sg.Text('SELECCIONE LAS LETRAS A CAMBIAR',justification='center',font=("Helvetica",10)),],       # Hay que aclarar tambien que esta funcion abre una nueva ventana.
            [sg.Listbox(values=letras,select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, size=(20, 12))],
            [sg.Button('Aceptar'),sg.Button('Salir')]]
    window = sg.Window('Cambiar letras', layout)
    event,values = window.read()
    x=letras
    while True:
        if event is None or event=='Salir':
            break
        else:
            x=cambiarAUX(values[0],letras,Bolsa)
            sg.popup('Sus nuevas letras son',letras)
            break        
    window.close()
    return x

def repartir(Bolsa):                                                                 # Funcion que selecciona una letra al azar de la bolsa,
    ok=True                                                                          # la descuenta de la misma y la devuelve.
    while ok:                                                                        
        letra = (random.choice([k for k in Bolsa for x in Bolsa[k]]))
        aux=int(Bolsa[letra][0])
        if aux > 0:
            Bolsa[letra][0]=aux-1
            ok=False
    return letra    

def obtenerColor(i,j):      # Funcion que obtiene una tupla de coordenadas y dependiendo cual sea devuelve un color especifico.
    if(i==0 and j==0)or(i==0 and j==7)or(i==0 and j==14)or(i==7 and j==0)or(i==7 and j==7)or(i==7 and j==14)or(i==14 and j==0)or(i==14 and j==7)or(i==14 and j==14):
        return(('white','green'))
    elif(i==0 and j==3)or(i==0 and j==11)or(i==1 and j==1)or(i==1 and j==13)or(i==2 and j==6)or(i==2 and j==8)or(i==3 and j==0)or(i==3 and j==3)or(i==3 and j==7)or(i==3 and j==11)or(i==3 and j==14)or(i==6 and j==1)or(i==6 and j==5)or(i==6 and j==9)or(i==6 and j==13)or(i==7 and j==3)or(i==7 and j==11)or(i==8 and j==1)or(i==8 and j==5)or(i==8 and j==9)or(i==8 and j==9)or(i==8 and j==13)or(i==11 and j==0)or(i==11 and j==3)or(i==11 and j==3)or(i==11 and j==7)or(i==11 and j==11)or(i==11 and j==14)or(i==12 and j==6)or(i==12 and j==6)or(i==12 and j==8)or(i==13 and j==1)or(i==13 and j==13)or(i==14 and j==3)or(i==14 and j==11):  
        return(('white','yellow'))
    elif(i==5 and j==4)or(i==5 and j==10)or(i==9 and j==4)or(i==9 and j==10):
        return(('white','red'))
    else:
        return(('white','white'))

def VerPosicion(event,x,y):     # Funcion para verificar, luego de ingresar 2 letras al tablero,
    if(event[0]==(x+1)):        # si se esta ingresando vertical u horizontalmente.
        return('Vertical')
    elif(event[1]==(y+1)):
        return('Horizontal')    

sg.theme('LightYellow')         # Tema/Fuente de la ventana (tablero).

MAX_Vector = 7                      
tam_celda =10                       # Variables que se utilizan para especificar el tipo de texto,
color_button = ('white','blue')     # botones, color, etc.
tam_button = 3,1 
MAX_ROWS = MAX_COL = 15

arcFichas=open('Fichas.json','r')       # Archivo .json que contiene un diccionario donde se
Bolsa = json.load(arcFichas)            # encuentra el puntaje y cantidad de cada ficha/letra.
arcFichas.close()

DicSumador={}                         # Se inicializa el diccionario donde se guardara las coordenadas con los colores de estas.

TableroDigital=[None]*15                
for i in range(0,15):
    TableroDigital[i]=[None]*15                # Se crea la matriz (TableroDigital) que sirve para ver donde se puede ingresar
for i in range(15):                            # una letra y donde no.
    for j in range(15):
        TableroDigital[i][j]= 'null'

FormarPalabra=''            # Variable que servira para ir formando la palabra en la jugada.

vector=[]
for pos in range(MAX_Vector):           # Se crea una lista (vector) donde se agregan las fichas que se reparten.
    a=repartir(Bolsa)                   # En este caso se reparten 7 fichas.
    vector.append(a)   

column1 = [[sg.Button('',size=(3, 1), key=(i,j), pad=(0,0),button_color=obtenerColor(i,j)) for j in range(MAX_COL)] for i in range(MAX_ROWS)]           # Columna que se crea el tablero para luego agregarlo al layout.

layout = [[sg.Button('Terminar Partida', size=(15,1)), sg.Text('Jugador: 0 pts', size=(23, 1), key=('Player'), justification='center', font=("Arial Black", 10), relief=sg.RELIEF_RIDGE), sg.Text(size=(10, 1), font=('Helvetica', 15), justification='center', key='-OUTPUT-')],
          [sg.Button('Posponer Partida', size=(15,1)), sg.Text('CPU: 0 pts', size=(23, 1), key=('CPU'), justification='center', font=("Arial Black", 10), relief=sg.RELIEF_RIDGE), sg.Button('Cambiar fichas', size=(15,1))],
          [sg.Button('?',size=(4, 2), pad=(0,0), button_color=('white','black')) for w in range(MAX_Vector)],
          [sg.Column(column1, background_color='#F7F3EC')],
          [sg.Button(vector[0], size=(4, 2), key=(0), pad=(0,0), button_color=('white','black')), sg.Button(vector[1], size=(4, 2), key=(1), pad=(0,0), button_color=('white','black')), sg.Button(vector[2], size=(4, 2), key=(2), pad=(0,0), button_color=('white','black')), sg.Button(vector[3], size=(4, 2), key=(3), pad=(0,0), button_color=('white','black')), sg.Button(vector[4], size=(4, 2), key=(4), pad=(0,0), button_color=('white','black')), sg.Button(vector[5], size=(4, 2), key=(5), pad=(0,0), button_color=('white','black')), sg.Button(vector[6], size=(4, 2), key=(6), pad=(0,0), button_color=('white','black'))],
          [sg.Button('Verificar palabra', size=(15,1)), sg.Button('Cancelar', size=(15,1))]]

# En el layout de arriba se organiza todos los botones y textos que tendra la ventana.

windowT = sg.Window('Scrabble', layout, size=(480,550), default_button_element_size=(3,1), auto_size_buttons=False)

# La linea de arriba crea la ventana y la inicializa con el layout creado.

arcConfi=open('TiempoyNivel.json','r')
TiempoNivel = json.load(arcConfi)
if TiempoNivel['0']:
    tiempo=60000
if TiempoNivel['1']:                      # Esta parte del codigo abre un archivo .json que contiene un diccionario
    tiempo=90000                          # especificando el tiempo de la partida y la dificultad. Estos datos se 
if TiempoNivel['2']:                      # utilizaran para programar la partida de una determinada manera.
    tiempo=120000  
if TiempoNivel['3']:
    nivel='facil'
if TiempoNivel['4']:
    nivel='medio'
if TiempoNivel['5']:
    nivel='dificil'         
arcConfi.close()        

arranca=random.randint(0,1)             # Esta parte del codigo hace un random para ver quien tiene la primera
if(arranca==1):                         # jugada (la cpu o el usuario).
    print('Empieza la CPU')
    #Funcion(paramentros) ---> Funcion que hace la jugada de la CPU
else:    
    print('Empieza el jugador')    

timer_running, counter = True, tiempo           # Se inicializa el contador del timer, y un String
letra_act=''                                    # que servira para diferentes partes del codigo. Este String tendra
                                                # la ficha actual que haya seleccionado el usuario.
while True:                  # Loop de la ventana. 
    event, values = windowT.read(timeout=10)
    if event == None or counter==0:
        break                                                        # En todo este loop se llaman a funciones o se realizan operaciones,
    if type(event) is tuple:                                         # dependiendo los values o los events.
        if(TableroDigital[event[0]][event[1]]=='null'):       
            if letra_act != '' and letra_act in vector:
                if(len(FormarPalabra)==0):
                    x=event[0]
                    y=event[1]
                    windowT[event].update(letra_act, button_color=('white','black'))
                    FormarPalabra=FormarPalabra+letra_act
                    TableroDigital[x][y]=letra_act
                    DicSumador[(x,y)]=obtenerColor(x,y)[1]
                    letra_act=''
                elif(len(FormarPalabra)==1):
                    if(event==(x+1,y) or event==(x,y+1)):
                        Orientacion=VerPosicion(event,x,y)
                        if(Orientacion=='Vertical'):
                            x=x+1
                        else:
                            y=y+1    
                        windowT[event].update(letra_act, button_color=('white','black'))
                        FormarPalabra=FormarPalabra+letra_act
                        TableroDigital[x][y]=letra_act
                        DicSumador[(x,y)]=obtenerColor(x,y)[1]
                        letra_act=''
                elif(len(FormarPalabra)>1):
                    if(Orientacion=='Vertical'):    
                        if(event==(x+1,y)):
                            x=x+1
                            windowT[event].update(letra_act, button_color=('white','black'))
                            FormarPalabra=FormarPalabra+letra_act
                            TableroDigital[x][y]=letra_act
                            DicSumador[(x,y)]=obtenerColor(x,y)[1]
                            letra_act='' 
                    if(Orientacion=='Horizontal'):  
                        if(event==(x,y+1)):
                            y=y+1
                            windowT[event].update(letra_act, button_color=('white','black'))
                            FormarPalabra=FormarPalabra+letra_act
                            TableroDigital[x][y]=letra_act
                            DicSumador[(x,y)]=obtenerColor(x,y)[1]
                            letra_act=''           
    elif event in range(0,7):
        letra_act=(windowT[event].GetText())
        keys_entered = event
        windowT[event].update('', button_color=('white','purple')) 
    if event == ('Terminar Partida'):
        if sg.popup_yes_no('Estas seguro?'):
            break
    if event == ('Posponer Partida'):
        sg.popup_yes_no('Estas seguro?')        # Falta implementar.
        pass
    if event == ('Cambiar fichas'):
        if sg.popup_yes_no('Estas seguro?'):
            NewLetras=CambiarFichas(Bolsa,vector)
            c=0
            for i in range(6):
                windowT[i].update(NewLetras[c])
                c=c+1
    if event == ('Verificar palabra'):
        if(len(FormarPalabra)>1 and verificarPalabra(FormarPalabra)):
            pts=(sumar(FormarPalabra,DicSumador,Bolsa))
            PtsJugador=(windowT.FindElement('Player').DisplayText)                  
            PtsJugador=PtsJugador.split(' ')
            Total=int(PtsJugador[1])
            Total=Total+pts
            Total=str(Total)
            windowT['Player'].update('Jugador: '+Total+' pts')
            for i in range(0,7):
                if(windowT[i].GetText()==''):
                    windowT[i].update(repartir(Bolsa), button_color=('white','black'))
            DicSumador={}
            FormarPalabra=''    
        else:
           FormarPalabra=cancelarPalabra(TableroDigital,DicSumador,FormarPalabra,letra_act)
           sg.popup('La palabra ingresada es incorrecta', font=('Helvatica', 10))    
    if event == 'Cancelar':
        FormarPalabra=cancelarPalabra(TableroDigital,DicSumador,FormarPalabra,letra_act)                
    if timer_running:
        windowT['-OUTPUT-'].update('{:02d}:{:02d}.{:02d}'.format((counter // 100) // 60, (counter // 100) % 60, counter % 100))
        counter -= 1  

windowT.close()         # Al finalizar el loop para cualquier razon se cierra la ventana y finaliza el programa.




# Godoy Francisco, Maurino Martin -----> Autores del programa.