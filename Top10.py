import PySimpleGUI as sg   
import json
def para_imprimir(event):
    """
    Esta funcion intenta abrir el archivo donde están los top10 dependiendo la dificultad que 
    el usuario eligió. Si el archivo no se encuentra salta una excepción con un popup manifestandolo.
        Parametros:
            event (str): Un string según la elección del ususario
        
        Retorna:
            data (list): Una lista de diccionarios con los mejores 10
    """

    if(event=='Fácil'):
        try:
            with open('top10facil.json', 'r') as archivo:
                data = json.load(archivo)
        except(Exception):
            sg.popup('No se encuentra el archivo top10facil.json, debe descargarlo')
    if(event=='Medio'):
        try:
            with open('top10medio.json', 'r') as archivo:
                data = json.load(archivo)
        except(Exception):
            sg.popup('No se encuentra el archivo top10medio.json, debe descargarlo')
    if(event=='Difícil'):
        try:
            with open('top10dificil.json', 'r') as archivo:
                data = json.load(archivo)
        except:
            sg.popup('No se encuentra el archivo top10dificil.json, debe descargarlo')
    return(data)

sg.theme('Light Yellow')
layout = [[sg.Text('   ELEGIR LA DIFICULTAD DE LA CUAL QUIERE VER LOS 10 MEJORES PUNTAJES',justification='center',font=("Ravie",11))],[sg.Button('Fácil',size=(14,3),font=("Ravie",12)),sg.Button('Medio',size=(14,3),font=("Ravie",12)),sg.Button('Difícil',size=(14,3),font=("Ravie",12)),sg.Exit(size=(14,3),font=("Ravie",12))]]      
window = sg.Window('Top 10', layout)    
x=True
while x==True:
    event, values = window.read() 
    if event is None or event=='Exit'or event=='Quit':
        x=False
    else:
        data=para_imprimir(event)
        for s in data:
            sg.Print(s,font='Ravie')
window.close()

# Autores: Francisco Godoy y Martín Maurino