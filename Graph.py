import PySimpleGUI as pg

# Step 1: Set theme
pg.theme("DarkAmber")

# Step 2: Create Layout
elem_layout = [
    [pg.Button("Add Element")],
]

# Step 3: Create Window
window = pg.Window("Form", elem_layout)


while True:
    event, values = window.read()
    if event == "Add Element":
        list_layout = [
            [pg.Multiline(size=(40,10), key='-LIST-')],
            [pg.Button("Oven")]
        ]
        window = pg.Window("List", list_layout)
        event, values = window.read()
        print(values[0])
    if event == pg.WIN_CLOSED:
        break
    print(values[0])

# Step 5: Close window
window.close()