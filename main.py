import csv
import PySimpleGUI as sg
from functions import *
import random
import pandas as pd

user = ""
cash = 0

# open_window function is a preset has to be changed, game window
def open_window():
    # geting data from data.csv and store it into a user_list
    with open("data.csv", "r") as file:
        data = file.readline()
        user_list = data.split(",")

    player_name = sg.Text(f"Player: {user_list[0]}", key='player')
    player_cash = sg.Text(f"Money: {int(user_list[1])}", key='p_cash')
    slots_result = sg.Text("", key='result')
    start_button = sg.Button("Start", key='start')
    menu_button = sg.Button("Return to main menu", key='ret_menu')
    close_button = sg.Button("Close", key='close')

    layout = [[player_name, player_cash], [slots_result], [start_button], [menu_button, close_button]]

    window = sg.Window("Second Window", layout, modal=True)
    choice = None

    while True:
        event, values = window.read()
        match event:
            case 'ret_menu':
                window.close()
                main()
            case 'close':
                break
            case sg.WIN_CLOSED:
                break

    window.close()

# launch window.
def main():

    label = sg.Text("Enter your name and press play.")
    user_input = sg.Input("", key='user', size=(51, 20),
                          do_not_clear=False)
    label2 = sg.Text("How much did you want to spend? ")
    user_cash = sg.Input("", key='cash', size=(20, 20),
                         do_not_clear=False)
    info_to_user = sg.Text("", key='to_user')
    confirm_button =sg.Button("Confirm", key='confirm')
    play_button = sg.Button("Play", key='play')
    exit_button = sg.Button("Exit", key='exit')

    layout = [[label],[user_input],[label2, user_cash],
              [confirm_button],
              [info_to_user],
              [play_button, exit_button]]

    launch_window = sg.Window("Menu", layout=layout,
                              font=("Hevetica", 10), size=(400,200), modal=True)
    choice = None

    while True:
        event, values = launch_window.read()
        match event:
            case 'confirm':
                # get a input value
                user = values['user']
                cash = values['cash']
                info_to_user.update(value=f"Hello {user} you store {cash} $")

                # user and cash stored in data.csv
                with open("data.csv", "w") as file:
                    file.writelines(f"{user},{cash}")
            case 'play':
                launch_window.close()
                open_window()
            case 'exit':
                break
            case sg.WIN_CLOSED:
                break
    launch_window.close()

if __name__ == "__main__":
    main()




