import PySimpleGUI as sg


def create_window(theme):
    sg.theme(theme)
    sg.set_options(font = 'Franklin 14', button_element_size = (90, 3))
    button_size = (6, 3)
    layout = [
        # You can also use sg.Push() for the same result :)
        [sg.Text(
            "",
            font = "Franklin 26",
            justification = 'right',
            expand_x = True,
            pad = (10, 20),
            right_click_menu = theme_menu,
            key = "-TEXT-"
            )
        ],
        [sg.Button("Clear", expand_x = True), sg.Button("Enter", expand_x = True)],
        [sg.Button(7, size = button_size), sg.Button(8, size = button_size), sg.Button(9, size = button_size), sg.Button("/", size = button_size)],
        [sg.Button(6, size = button_size), sg.Button(5, size = button_size), sg.Button(4, size = button_size), sg.Button("*", size = button_size)],
        [sg.Button(1, size = button_size), sg.Button(2, size = button_size), sg.Button(3, size = button_size), sg.Button("-", size = button_size)],
        [sg.Button(0, expand_x = True), sg.Button(".", size = button_size), sg.Button("+", size = button_size)]
    ]

    return sg.Window('Calculator', layout)

theme_menu = ["menu", ["LightGray1", "dark", "DarkGrey8", "random"]]
window = create_window("dark")

current_num = []
full_op = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)

    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        current_num.append(event)
        num_str = ''.join(current_num)
        window['-TEXT-'].update(num_str)

    if event in ['+', '-' , '/', '*']:
        full_op.append(''.join(current_num))
        current_num = []
        full_op.append(event)
        window['-TEXT-'].update("")

    if event == "Enter":
        full_op.append(''.join(current_num))
        result = eval(" ".join(full_op))
        window['-TEXT-'].update(result)
        full_op = []

    if event == "Clear":
        current_num = []
        full_op = []
        window['-TEXT-'].update("")

window.close()
