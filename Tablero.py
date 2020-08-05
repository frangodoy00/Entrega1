import PySimpleGUI as sg        # Importacion de los paquetes que son necesarios para la ejecucion
import json                     # del programa.
import random
from itertools import permutations
from datetime import datetime
from operator import itemgetter
import pattern.es

def verificarPalabra(palabra,nivel):                  # Esta funcion recibe un String y verifica si la palabra    
    pal=palabra.lower()                         # ingresada es correcta o no.
    ok=False
    if nivel=='facil':
        if pal in pattern.es.lexicon:
            if pal in pattern.es.spelling:
                ok=True
    if nivel=='medio':
        if pal in pattern.es.lexicon:
            if pal in pattern.es.spelling:
                dato = pattern.es.parse(pal,tokenize = True,tags = True,chunks = False).replace(pal,'')
                if dato in '/JJ':
                    ok=True
                if pal in pattern.es.verbs:
                    ok=True
    if nivel=='dificil':
        if pal in pattern.es.lexicon:
            if pal in pattern.es.spelling:
                if pal in pattern.es.verbs:
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

def obtenerColor(nivel,i,j):      # Funcion que obtiene una tupla de coordenadas y dependiendo cual sea devuelve un color especifico.
    if(nivel=='facil'):
        if(i==0 and j==0)or(i==0 and j==7)or(i==0 and j==14)or(i==7 and j==0)or(i==7 and j==7)or(i==7 and j==14)or(i==14 and j==0)or(i==14 and j==7)or(i==14 and j==14):
            return(('white','green'))
        elif(i==0 and j==3)or(i==0 and j==11)or(i==1 and j==1)or(i==1 and j==13)or(i==2 and j==6)or(i==2 and j==8)or(i==3 and j==0)or(i==3 and j==3)or(i==3 and j==7)or(i==3 and j==11)or(i==3 and j==14)or(i==6 and j==1)or(i==6 and j==5)or(i==6 and j==9)or(i==6 and j==13)or(i==7 and j==3)or(i==7 and j==11)or(i==8 and j==1)or(i==8 and j==5)or(i==8 and j==9)or(i==8 and j==9)or(i==8 and j==13)or(i==11 and j==0)or(i==11 and j==3)or(i==11 and j==3)or(i==11 and j==7)or(i==11 and j==11)or(i==11 and j==14)or(i==12 and j==6)or(i==12 and j==6)or(i==12 and j==8)or(i==13 and j==1)or(i==13 and j==13)or(i==14 and j==3)or(i==14 and j==11):  
            return(('white','yellow'))
        elif(i==5 and j==4)or(i==5 and j==10)or(i==9 and j==4)or(i==9 and j==10):
            return(('white','red'))
        else:
            return(('white','white'))
    elif(nivel=='medio'):
        if(i==0 and j==0)or(i==0 and j==14)or(i==7 and j==0)or(i==7 and j==14)or(i==14 and j==0)or(i==14 and j==14):
            return(('white','green'))
        elif(i==0 and j==3)or(i==0 and j==11)or(i==1 and j==1)or(i==1 and j==13)or(i==2 and j==6)or(i==2 and j==8)or(i==3 and j==0)or(i==3 and j==7)or(i==3 and j==14)or(i==6 and j==1)or(i==6 and j==5)or(i==6 and j==9)or(i==6 and j==13)or(i==8 and j==1)or(i==8 and j==5)or(i==8 and j==9)or(i==8 and j==9)or(i==8 and j==13)or(i==11 and j==0)or(i==11 and j==7)or(i==11 and j==14)or(i==12 and j==6)or(i==12 and j==6)or(i==12 and j==8)or(i==13 and j==1)or(i==13 and j==13)or(i==14 and j==3)or(i==14 and j==11):  
            return(('white','yellow'))
        elif(i==7 and j==7)or(i==3 and j==3)or(i==3 and j==11)or(i==7 and j==3)or(i==7 and j==11)or(i==11 and j==3)or(i==11 and j==11)or(i==5 and j==4)or(i==5 and j==10)or(i==9 and j==4)or(i==9 and j==10):
            return(('white','red'))
        else:
            return(('white','white'))
    else:
        if(i==0 and j==0)or(i==0 and j==14)or(i==14 and j==0)or(i==14 and j==14):
            return(('white','green'))
        elif(i==0 and j==3)or(i==0 and j==11)or(i==1 and j==1)or(i==2 and j==6)or(i==2 and j==8)or(i==3 and j==0)or(i==3 and j==7)or(i==3 and j==14)or(i==6 and j==5)or(i==6 and j==9)or(i==8 and j==5)or(i==8 and j==9)or(i==8 and j==9)or(i==11 and j==0)or(i==11 and j==7)or(i==11 and j==14)or(i==12 and j==6)or(i==12 and j==6)or(i==12 and j==8)or(i==14 and j==3)or(i==14 and j==11):  
            return(('white','yellow'))
        elif(i==7 and j==7)or(i==3 and j==3)or(i==3 and j==11)or(i==1 and j==1)or(i==1 and j==13)or(i==7 and j==3)or(i==6 and j==1)or(i==6 and j==13)or(i==7 and j==11)or(i==8 and j==1)or(i==8 and j==13)or(i==11 and j==3)or(i==11 and j==11)or(i==5 and j==4)or(i==5 and j==10)or(i==9 and j==4)or(i==9 and j==10)or(i==13 and j==1)or(i==13 and j==13):
            return(('white','red'))
        else:
            return(('white','white'))



def VerPosicion(event,x,y):     # Funcion para verificar, luego de ingresar 2 letras al tablero,
    if(event[0]==(x+1)):        # si se esta ingresando vertical u horizontalmente.
        return('Vertical')
    elif(event[1]==(y+1)):
        return('Horizontal')    

def ActualizarTop(nivel,puntos):       # Función para actualizar el top dependiendo el nivel de dificultad
    if(nivel=='facil'):
        dicc={}
        with open('top10facil.json', 'r') as archivo:
            data = json.load(archivo)
        if data[9]["puntos"]<puntos:
            archivo = open("nombre.txt", 'r')
            for linea in archivo.readlines():
                l=linea
            now = datetime.now()
            fecha= now.strftime('Dia :%d, Mes: %m, Anio: %Y, Hora: %H, Minutos: %M, Segundos: %S')
            dicc={'nombre':l,"puntos":puntos,"fecha":fecha}
            data[9]=dicc
            ord=sorted(data, key=itemgetter('puntos'),reverse=True)
            with open('top10facil.json', 'w') as archivo:
                json.dump(ord, archivo) 
    elif(nivel=='medio'):
        dicc={}
        with open('top10medio.json', 'r') as archivo:
            data = json.load(archivo)
        if data[9]["puntos"]<puntos:
            archivo = open("nombre.txt", 'r')
            for linea in archivo.readlines():
                l=linea
            now = datetime.now()
            fecha= now.strftime('Dia :%d, Mes: %m, Anio: %Y, Hora: %H, Minutos: %M, Segundos: %S')
            dicc={'nombre':l,"puntos":puntos,"fecha":fecha}
            data[9]=dicc
            ord=sorted(data, key=itemgetter('puntos'),reverse=True)
            with open('top10medio.json', 'w') as archivo:
                json.dump(ord, archivo) 
    else:
        dicc={}
        with open('top10dificil.json', 'r') as archivo:
            data = json.load(archivo)
        if data[9]["puntos"]<puntos:
            archivo = open("nombre.txt", 'r')
            for linea in archivo.readlines():
                l=linea
            now = datetime.now()
            fecha= now.strftime('Dia :%d, Mes: %m, Anio: %Y, Hora: %H, Minutos: %M, Segundos: %S')
            dicc={'nombre':l,"puntos":puntos,"fecha":fecha}
            data[9]=dicc
            ord=sorted(data, key=itemgetter('puntos'),reverse=True)
            with open('top10dificil.json', 'w') as archivo:
                json.dump(ord, archivo) 

def ganador(puntos,puntospc):
    if(puntospc<puntos):
        sg.popup('GANASTE, FELICITACIONES!!!')
    elif(puntos==puntospc):
        sg.popup('EMPATEEE!!!')
    else:
        sg.popup('PERDISTE :(')

def puntajes(lista):                                           # Función para obtener los puntajes del jugador y la CPU
    PtsJugador=(windowT.FindElement('Player').DisplayText)                  
    PtsJugador=PtsJugador.split(' ')
    TotalJ=int(PtsJugador[1]) 
    PtsPc=(windowT.FindElement('CPU').DisplayText)                  
    PtsPc=PtsPc.split(' ')
    TotalPC=int(PtsPc[1]) 
    lista.append(TotalJ)
    lista.append(TotalPC)
def comparar():
    claves = list(Bolsa.values())                    # Función para verificar si la Bolsa está vacía
    x=True
    c=0
    for cla in claves:
        if cla[0]==0:
            c=c+1
    if(c==26):
        x=False
    return(x)

def Posponer(lista,nivel,Bolsa,TableroDigital,vector,vectorpc):    # Esta función guarda en archivos los datos necesarios en caso de que se seleccione
    archivo = open("nombre.txt", 'r')                              # en caso de que se seleccione el botón de posponer partida
    for linea in archivo.readlines():
        l=linea
    lista.append(l)
    lista.append(nivel)
    tablero=[None]*15                
    for i in range(0,15):
        tablero[i]=[None]*15    
    for i in range(15):                            
        for j in range(15):
            tablero[i][j]= 'null'
    colores={}
    atrilJ=[]
    atrilPC=[]
    with open('datosPosponer.json', 'w') as arch:
        json.dump(lista, arch) 
    with open('bolsaGuardada.json','w') as arc:
        json.dump(Bolsa,arc)
    for x in range(15):
        for y in range(15):
            tablero[x][y] = TableroDigital[x][y]
    with open('guardarTablero.json','w')as ar:
        json.dump(tablero,ar)
    for x in range(7):
        atrilJ.append(vector[x])
        atrilPC.append(vectorpc[x])
    with open('atrilJ.json','w')as a:
        json.dump(atrilJ,a)
    with open('atrilPC.json','w')as a:
        json.dump(atrilPC,a)

def abrirPartida(TableroDigital,Bolsa,vector,vectorpc):
    with open('datosPosponer.json','r')as arc:
        data=json.load(arc)
    with open('bolsaGuardada.json','r') as ar:
        Bolsa = json.load(ar)
    with open('guardarTablero.json','r')as ar:
        tablero= json.load(ar)
    with open('atrilJ.json','r')as a:
        vector=json.load(a)
    with open('atrilPC.json','r')as b:
        vectorpc=json.load(b)
    for x in range(7):
        windowT[x].update(vector[x])
    for x in range(15):
        for y in range(15):
            TableroDigital[x][y]=tablero[x][y]
            windowT[(x,y)].update('',button_color=(obtenerColor(data[5],x,y)))
            if tablero[x][y]!='null':
                windowT[(x,y)].update(tablero[x][y],button_color=('white','black'))
    Total=str(data[2])
    windowT['Player'].update('Jugador: '+Total+' pts')
    Totalpc=str(data[3])
    windowT['CPU'].update('CPU: '+Totalpc+' pts')
    timer_running, counter = True, data[0]  
    archivo=open('nombre.txt','w')
    archivo.write(data[4])
    archivo.close()
    cont=data[1]
    return(timer_running,counter,cont,vector)

def generarPalabraCPU(atril,nivel):
    letras = ''
    for letra in atril:
        letras += letra
    palabras = set()
    for i in range(2, len(letras) + 1):
        palabras.update((map("".join, permutations(letras, i))))
    palabras_validas = []
    for pal in palabras:
        if verificarPalabra(pal,nivel):
            palabras_validas.append(pal)
    if(palabras_validas):
        return(palabras_validas[0])
    else:
        print('La cpu no pudo generar ninguna palabra')
        return None

def PrimeraMano(vector,atril_cpu,MAX_Vector):
    for pos in range(MAX_Vector):           # Se crean 2 listas (vector) donde se agregan las fichas que se reparten.
        a=repartir(Bolsa)                   # En este caso se reparten 7 fichas.
        vector.append(a)
        a=repartir(Bolsa)
        atril_cpu.append(a)

def IniciarTiempoyNivel():
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
    return (tiempo,nivel)

def verificarLugar(palabra,TableroDigital):         # Esta funcion es la que realiza un random para ver donde colocar
    num=15-len(palabra)                             # la palabra de la CPU, en caso de ser posible. Devuelve la coordenada
    ok=False                                        # de la primera letra y la orientacion (vertical u horizontal)
    while(not ok):
        ok=True
        orientacion=random.randint(0,1)
        corX=X=random.randint(0,num)  
        corY=Y=random.randint(0,num)
        for i in range(len(palabra)):
            if(TableroDigital[X][Y]!='null'):
                ok=False
            if(orientacion==0):
                X=X+1
            else:
                Y=Y+1
    X=corX
    Y=corY
    for i in range(len(palabra)):
        TableroDigital[X][Y]=palabra[i]
        if(orientacion==0):
            X=X+1
        else:
            Y=Y+1
    return(orientacion,corX,corY) 

def repartir_cpu(atril,palabra,bolsa):
    for i in range(len(palabra)):               # Esta funcion le reparte fichas nuevas a la CPU, intercambiandolas
        ok=False                                # por las fichas anteriormente utilizadas.
        pos=0
        while(not ok):
            if(palabra[i]==atril[pos]):
                atril[pos]=repartir(bolsa)
                ok=True
            else:
                pos=pos+1    
            
def TurnoCPU(atril_cpu,nivel,TableroDigital,DicSumador,Bolsa):
        palabra_cpu=generarPalabraCPU(atril_cpu,nivel)
        datos_coor=verificarLugar(palabra_cpu,TableroDigital)
        orientacion=datos_coor[0]
        coorX=datos_coor[1]
        coorY=datos_coor[2]
        for i in range(len(palabra_cpu)):
            windowT[(coorX,coorY)].update(palabra_cpu[i], button_color=('white','black'))
            DicSumador[(coorX,coorY)]=obtenerColor(nivel,coorX,coorY)[1]
            if(orientacion==0):
                coorX=coorX+1
            else:
                coorY=coorY+1    
        pts=(sumar(palabra_cpu,DicSumador,Bolsa))
        PtsCPU=(windowT.FindElement('CPU').DisplayText)                  
        PtsCPU=PtsCPU.split(' ')
        Total=int(PtsCPU[1])
        Total=Total+pts
        Total=str(Total)
        windowT['CPU'].update('CPU: '+Total+' pts')
        DicSumador={}
        repartir_cpu(atril_cpu,palabra_cpu,Bolsa)

def FinDePartida():
            lis=[]
            puntajes(lis)
            ActualizarTop(nivel,lis[0])
            ganador(lis[0],lis[1])

def TurnoJugador(FormarPalabra,letra_act,TableroDigital,DicSumador,Orientacion,x,y):
    if(len(FormarPalabra)==0):
        x=event[0]
        y=event[1]
        windowT[event].update(letra_act, button_color=('white','black'))
        FormarPalabra=FormarPalabra+letra_act
        TableroDigital[x][y]=letra_act
        DicSumador[(x,y)]=obtenerColor(nivel,x,y)[1]
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
            DicSumador[(x,y)]=obtenerColor(nivel,x,y)[1]
            letra_act=''
    elif(len(FormarPalabra)>1):
        if(Orientacion=='Vertical'):    
            if(event==(x+1,y)):
                x=x+1
                windowT[event].update(letra_act, button_color=('white','black'))
                FormarPalabra=FormarPalabra+letra_act
                TableroDigital[x][y]=letra_act
                DicSumador[(x,y)]=obtenerColor(nivel,x,y)[1]
                letra_act='' 
        if(Orientacion=='Horizontal'):  
            if(event==(x,y+1)):
                y=y+1
                windowT[event].update(letra_act, button_color=('white','black'))
                FormarPalabra=FormarPalabra+letra_act
                TableroDigital[x][y]=letra_act
                DicSumador[(x,y)]=obtenerColor(nivel,x,y)[1]
                letra_act=''                
    return(FormarPalabra,letra_act,Orientacion,x,y)

def GuardarPartida(nivel,Bolsa,TableroDigital,vector,atril_cpu):
    lis=[]
    lis.append(counter)
    lis.append(cont_cambiarFichas)
    puntajes(lis)
    archivo=open("partidaGuardada.txt", 'w')
    archivo.write("si") 
    archivo.close()
    Posponer(lis,nivel,Bolsa,TableroDigital,vector,atril_cpu)

def SustituirFichas(cont_cambiarFichas,Bolsa,vector):
    cont_cambiarFichas=cont_cambiarFichas+1
    NewLetras=CambiarFichas(Bolsa,vector)
    c=0
    for i in range(6):
        windowT[i].update(NewLetras[c])
        vector[c]=NewLetras[c]
        c=c+1
    if(cont_cambiarFichas==3):
        windowT['Cambiar fichas'].update(disabled=(True))
    return cont_cambiarFichas

def Verificando(FormarPalabra,nivel,DicSumador,Bolsa,vector,ok,TableroDigital,letra_act):
    if(len(FormarPalabra)>1 and verificarPalabra(FormarPalabra,nivel)):
        ok=True
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
                vector[i]=windowT[i].GetText()
        DicSumador={}
        FormarPalabra=''       
    else:
        ok=False
        FormarPalabra=cancelarPalabra(TableroDigital,DicSumador,FormarPalabra,letra_act)
        sg.popup('La palabra ingresada es incorrecta', font=('Helvatica', 10))
    return(ok,FormarPalabra,letra_act)    

sg.theme('LightYellow')         # Tema/Fuente de la ventana (tablero)

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
atril_cpu=[]
PrimeraMano(vector,atril_cpu,MAX_Vector)
   
(tiempo,nivel)=IniciarTiempoyNivel()   

column1 = [[sg.Button('',size=(3, 1), key=(i,j), pad=(0,0),button_color=obtenerColor(nivel,i,j)) for j in range(MAX_COL)] for i in range(MAX_ROWS)]           # Columna que se crea el tablero para luego agregarlo al layout.

layout = [[sg.Button('Terminar Partida', size=(15,1)), sg.Text('Jugador: 0 pts', size=(23, 1), key=('Player'), justification='center', font=("Arial Black", 10), relief=sg.RELIEF_RIDGE), sg.Text(size=(10, 1), font=('Helvetica', 15), justification='center', key='-OUTPUT-')],
          [sg.Button('Posponer Partida', size=(15,1)), sg.Text('CPU: 0 pts', size=(23, 1), key=('CPU'), justification='center', font=("Arial Black", 10), relief=sg.RELIEF_RIDGE), sg.Button('Cambiar fichas', size=(15,1))],
          [sg.Button('?',size=(4, 2), pad=(0,0), button_color=('white','black')) for w in range(MAX_Vector)],
          [sg.Column(column1, background_color='#F7F3EC')],
          [sg.Button(vector[0], size=(4, 2), key=(0), pad=(0,0), button_color=('white','black')), sg.Button(vector[1], size=(4, 2), key=(1), pad=(0,0), button_color=('white','black')), sg.Button(vector[2], size=(4, 2), key=(2), pad=(0,0), button_color=('white','black')), sg.Button(vector[3], size=(4, 2), key=(3), pad=(0,0), button_color=('white','black')), sg.Button(vector[4], size=(4, 2), key=(4), pad=(0,0), button_color=('white','black')), sg.Button(vector[5], size=(4, 2), key=(5), pad=(0,0), button_color=('white','black')), sg.Button(vector[6], size=(4, 2), key=(6), pad=(0,0), button_color=('white','black'))],
          [sg.Button('Verificar palabra', size=(15,1)), sg.Button('Cancelar', size=(15,1))]]

# En el layout de arriba se organiza todos los botones y textos que tendra la ventana.

windowT = sg.Window('Scrabble', layout, size=(480,550), default_button_element_size=(3,1), auto_size_buttons=False)
 
# La linea de arriba crea la ventana y la inicializa con el layout creado.

cont_cambiarFichas=0
timer_running, counter = True, tiempo           # Se inicializa el contador del timer, y un String
letra_act=''                                    # que servira para diferentes partes del codigo. Este String tendra
Orientacion=''                                  # la ficha actual que haya seleccionado el usuario.
x=0
y=0  
ok=False                                              

arranca=random.randint(0,1)                 # Esta parte del codigo hace un random para ver quien tiene la primera
event, values = windowT.read(timeout=10)    # jugada (la cpu o el usuario).
ar = open('partidaGuardada.txt','r')
for linea in ar.readlines():                    # Se abre el archivo para verificar si existe una partida guardada
    c=linea
if (c=='si'):
    (timer_running,counter,cont_cambiarFichas,vector)=abrirPartida(TableroDigital,Bolsa,vector,atril_cpu)
    archivo = open("partidaGuardada.txt", 'w')
    archivo.write("no")
    arranca=0 

if(arranca==1):                         
    print('Empieza la CPU')
    TurnoCPU(atril_cpu,nivel,TableroDigital,DicSumador,Bolsa)
    DicSumador={}
else:    
    print('Empieza el jugador')    


while True:                  # Loop de la ventana. 
    event, values = windowT.read(timeout=10)
    if event== None:             # Compara si el evento es None, actualiza el top e imprime el ganador
        FinDePartida()
        break
    if counter==0:               # Verifica si el tiempo terminó, actualiza el top e imprime el ganador
        FinDePartida()        
        break
    if comparar()==False:        # Llama a la función comparar que comprueba si la bolsa está vacía,
        FinDePartida()  
        break
                                                             # En todo este loop se llaman a funciones o se realizan operaciones,
    if type(event) is tuple:                                         # dependiendo los values o los events.
        if(TableroDigital[event[0]][event[1]]=='null'):       
            if letra_act != '' and letra_act in vector:
                (FormarPalabra,letra_act,Orientacion,x,y)=TurnoJugador(FormarPalabra,letra_act,TableroDigital,DicSumador,Orientacion,x,y)           
    elif event in range(0,7):
        windowT['Posponer Partida'].update(disabled=True)
        letra_act=(windowT[event].GetText())
        windowT[event].update('', button_color=('white','purple')) 
    if event == ('Terminar Partida'):
        if (sg.popup_yes_no('Estas seguro?'))=='Yes':
            FinDePartida()
            break
    if event == ('Posponer Partida'):
        if (sg.popup_yes_no('Estas seguro?'))=='Yes':
            GuardarPartida(nivel,Bolsa,TableroDigital,vector,atril_cpu)
            break
        else:
            pass    
    if event == ('Cambiar fichas'):
        if (sg.popup_yes_no('Estas seguro?'))=='Yes':
            cont_cambiarFichas=SustituirFichas(cont_cambiarFichas,Bolsa,vector) 
            TurnoCPU(atril_cpu,nivel,TableroDigital,DicSumador,Bolsa)
            DicSumador={}
    if event == ('Verificar palabra'):
        windowT['Posponer Partida'].update(disabled=False)
        (ok,FormarPalabra,letra_act)=Verificando(FormarPalabra,nivel,DicSumador,Bolsa,vector,ok,TableroDigital,letra_act)
        if ok:
            TurnoCPU(atril_cpu,nivel,TableroDigital,DicSumador,Bolsa)
            DicSumador={}
    if event == 'Cancelar':
        windowT['Posponer Partida'].update(disabled=False)
        FormarPalabra=cancelarPalabra(TableroDigital,DicSumador,FormarPalabra,letra_act)                
    if timer_running:
        windowT['-OUTPUT-'].update('{:02d}:{:02d}.{:02d}'.format((counter // 100) // 60, (counter // 100) % 60, counter % 100))
        counter -= 1  

windowT.close()         # Al finalizar el loop para cualquier razon se cierra la ventana y finaliza el programa.




# Godoy Francisco, Maurino Martin -----> Autores del programa.