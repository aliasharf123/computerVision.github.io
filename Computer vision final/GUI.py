import os

import PySimpleGUI as sg
from predicate import detect_boxes
layout = [
    [sg.Text('Choose Your Image'), sg.Input(), sg.FileBrowse(key="-file-")],
    [sg.Button("submit"), sg.Button("classify")],
    [sg.Image(key="-image-")],
    [sg.Text(key="-uw-")]

]
window = sg.Window('ITI computer vision final project', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        print('closed')
        break
    if event == "submit":
        print("kfs;lk")

        print(values)
        if os.path.exists(values["-file-"]):
            image = values["-file-"]
            window["-image-"].update(image)
    if event == "classify":
        print(values)
        window["-uw-"].update(detect_boxes(values["-file-"]))

