import PySimpleGUI as sg
import json

def conFichas():
    """
    Define la ventana para modificar la cantidad y el valor de las fichas por cada letra.
    El usuario puede elegir en la letra en la listbox y modificar los valores. 
    En caso de ingresar un string en lugar de un integer salta un popup.
    Las modificaciones se guardan en el archivo Fichas.json al ingresar Save
    """
    sg.theme('LightYellow')
    choices = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    
    column1 = [[sg.Text('Fichas:', background_color='#F7F3EC', justification='center', size=(10, 1), font=("Ravie", 15))],      
            [sg.Text('Cantidad:', size=(15, 1),font=("Ravie")), sg.InputText()],     
            [sg.Text('Puntos:', size=(15, 1),font=("Ravie")), sg.InputText()],
            [sg.Button('Save',font=("Ravie")), sg.Button('Exit',font=("Ravie"))]]
    
    layout = [[sg.Text('Que letra desea modificar?', font=("Ravie", 15))],
            [sg.Listbox(choices, size=(8, 9), key='letra', enable_events=True,font=("Ravie"),text_color='lightyellow'),
             sg.Column(column1, background_color='#F7F3EC')] ]

    windowF = sg.Window('Scrabble', layout)
    try:
        arcFICHAS=open('Fichas.json','r')
        letras = json.load(arcFICHAS)
        arcFICHAS.close()
    except(Exception):
        sg.popup('No se encuentra el archivo Fichas.json, debe descargarlo')
    while True:                  # the event loop
        event, values = windowF.read()
        if event in (None, 'Exit'):      
            break
        if values['letra']:    
           if event == ('Save'):
                if(values[0].isdigit())and(values[1].isdigit()):
                    letras[values['letra'][0]]=(values[0],values[1])
                else:
                   sg.popup('Solo puede ingresar números')
    windowF.close()
    arcFICHAS=open('Fichas.json','w')
    json.dump(letras, arcFICHAS)
    arcFICHAS.close()


def configuracion():
    """
    Esta función define la ventana donde se puede seleccionar el tiempo y el nivel a elegir.
    La selección se guarda en el archivo TiempoyNivel.json al seleccionar el botón GUARDAR.
    Al seleccionar el botón FICHAS se abre otra ventana.
    """
    sg.theme('LightYellow')

    layout = [[sg.Text('CONFIGURACION', size=(25, 1), justification='center', font=("Ravie", 25), relief=sg.RELIEF_RIDGE)],            
          [sg.Text('TIEMPO:', size=(40,1), justification='center', font=("Ravie", 15))],
          [sg.Radio('10 minutos', 'time', size=(21,1), font=("Ravie", 10)), sg.Radio('15 minutos', 'time', size=(22,1), font=("Ravie", 10), default=True), sg.Radio('20 minutos', 'time', font=("Ravie", 10))],           
          [sg.Text('NIVEL:', size=(40,1), justification='center', font=("Ravie", 15))],            
          [sg.Radio('Facil', 'nivel', size=(21,1), font=("Ravie", 10)),  sg.Radio('Medio', 'nivel', size=(22,1), font=("Ravie", 10), default=True), sg.Radio('Dificil', 'nivel', font=("Ravie", 10))],
          [sg.Button('GUARDAR',font="Ravie"), sg.Button('FICHAS',font="Ravie")]]

    windowC = sg.Window('Scrabble', layout)      
    
    while True:                             # Loop
       event, values = windowC.read()       
       if event == None:      
            break  
       if event == ('GUARDAR'):
            arcConfi=open('TiempoyNivel.json','w')
            TiempoNivel=values
            json.dump(TiempoNivel, arcConfi)
            arcConfi.close()
            break   
       if event == ('FICHAS'):
           conFichas()

    windowC.close()
    
configuracion()

# Autores: Francisco Godoy y Martín Maurino