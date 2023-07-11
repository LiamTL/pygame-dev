# Return to 1:09:58

import PySimpleGUI as sg

layout = [[]]

window = sg.Window("Stopwatch", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
