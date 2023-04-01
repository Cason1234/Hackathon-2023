import PySimpleGUI as sg


elem_layout = [
    [sg.Button("Add Element")],
]

elem_window = sg.Window("Form", elem_layout)


# Event loop
while True:
    event, values = elem_window.read()
    if event == "Add Element":
        button_list = ['Oven',
                       'Microwave',
                       'Fireplace',
                       'Heater']
        button_layout = [[sg.Listbox(values=button_list, size=(20, 10), select_mode='double')]]

        window = sg.Window("List", button_layout)

        event, values = window.read()
        print(values[0])
        if event == "Oven":
            break
    if event == sg.WINDOW_CLOSED:
        break

# Close the window
elem_window.close()
