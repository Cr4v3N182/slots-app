import PySimpleGUI as sg
import random

user_name = ""
cash = 0

label = sg.Text("Enter your name and press play.")
user_input = sg.InputText("", key='user')
label2 = sg.Text("How much did you want to spend?")
user_cash = sg.Input("", key='cash')
info_to_user = sg.Text("", key='to_user')
play_button = sg.Button("Play", key='play')
exit_button = sg.Button("Exit", key='exit')

layout = [[label],[user_input],[label2, user_cash],[play_button, exit_button]]

launch_window = sg.Window("Menu", layout=layout, font="Hevetica", size=(400,200))

while True:
    event, values = launch_window.read()
    match event:
        case 'exit':
            break
        case sg.WIN_CLOSED:
            break




