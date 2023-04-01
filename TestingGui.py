import PySimpleGUI as sg

# Define the layout
button_list = [f'Button {i}' for i in range(20)]
layout = [[sg.Listbox(values=button_list, size=(20, 10), select_mode='single')]]

# Create the window
window = sg.Window('Scrolling Buttons', layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

# Close the window
window.close()
