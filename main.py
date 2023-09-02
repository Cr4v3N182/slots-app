import PySimpleGUI as sg
import random

user = ""
cash = 0

# open_window function is a preset has to be changed
def open_window():
    layout = [[sg.Text("New Window", key="new")]]
    window = sg.Window("Second Window", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()


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
                user = values['user']   # get a input value
                cash = values['cash']
                info_to_user.update(value=f"Hello {user} you store {cash} $")
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




