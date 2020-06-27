import PySimpleGUI as sg

def IngresandoNombre():
    """
    Esta función define la ventana para que el usuario pueda ingresar su nombre y dos botones: aceptar y exit
    """
    sg.theme('LightYellow')
    layout = [
    [sg.Text('Ingrese su nombre:', size=(15, 1),font=("Ravie")), sg.InputText()],
    [sg.Button('Aceptar',font=("Ravie")), sg.Button('Exit',font=("Ravie"))]
    ]
    windowN = sg.Window('Scrabble', layout)
    event, values = windowN.read()
    ok=False
    if event == ('Aceptar'):
        ok=True
    if event == ('Exit'):
        pass        
    windowN.close()
    return ok
def partida():
    """
    Esta funcion define la ventana que se abrirá si el usuario toca el botón iniciar en el menú principal
    La ventana le dará a elegir al usuario si quiere continuar una partida o iniciar una nueva. Si es 
    posible podrá continuar la partida, en caso contrario saltará un popup que dirá que no hay una
    partida guardada. Si inicia una nueva deberá ingresar su nombre y se abrirá la ventana para jugar
    """
    sg.theme('LightYellow')
    layout = [[sg.Button('Continuar', size=(20,3),font=("Ravie"))],
          [sg.Button('Partida Nueva', size=(20,3),font=("Ravie"))]]
    windowP = sg.Window('Scrabble', layout)
    while True:
        event, values = windowP.read()
        if event == ('Partida Nueva'):
            ok=IngresandoNombre()
            if ok:
                import Tablero
            break 
        if event == ('Continuar'):
            sg.popup('No hay ninguna partida guardada')        
    windowP.close()

sg.theme('LightYellow')

layout = [[sg.T('',size=(1,3))],
          [sg.Text('Scrabble', size=(30, 3), justification='center', font=("Ravie", 25))],
          [sg.T(' ' * 18), sg.Button('Iniciar', size=(18,2), border_width=(30),font=("Ravie", 12))],
          [sg.T(' ', size=(1,5))],
          [sg.Button('Top 10', size=(15,2),font=('Ravie',10)), sg.T(' ' * 35), sg.Button('Configuracion', size=(15,2),font=("Ravie", 10))]]

windowM = sg.Window('Scrabble', layout, size=(500, 475))

while True:                  # the event loop
    event, values = windowM.read()
    if event == None:      
        break
    if event == ('Configuracion'):
        import Configuracion    
    if event == ('Top 10'):
        import Top10
    if event == ('Iniciar'):
        partida()
        break

windowM.close()

# Autores: Francisco Godoy y Martín Maurino