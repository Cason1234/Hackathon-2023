import PySimpleGUI as pg

# Step 1: Set theme
pg.theme("DarkAmber")

# Step 2: Create Layout
layout = [
    [pg.Button("Add Element")]
]

# Step 3: Create Window
window = pg.Window("Carbon Footprint Calculator", layout)

# Step 4: Event loop
while True:
    event, values = window.read()
    if event == pg.WIN_CLOSED:
        break
    if event == "Add Element":
        options = ["Oven", "Microwave", "TV"]
        list_layout = [[pg.OptionMenu(values=options)],
                       [pg.Button("Ok")]]
        window = pg.Window('Options For whatever', list_layout)
        event, values = window.read()
    if  event == "Ok":
        print(values[0])
        layout = [
            [pg.Button("1 hour")],
            [pg.Button("2 hour")],
        ]
        window = pg.Window("Times", layout)
        event, values = window.read()

    #print(values[0])

# Step 5: Close window
window.close()

