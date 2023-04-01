import PySimpleGUI as pg

# Step 1: Set theme
pg.theme("DarkAmber")

# Step 2: Create Layout
layout = [
    [pg.Text("Enter name")],
    [pg.InputText()],
    [pg.Button("Ok"), pg.Button("Cancel")]
]

# Step 3: Create Window
window = pg.Window("Form", layout)

# Step 4: Event loop
while True:
    event, values = window.read()
    if event == "Cancel" or event == pg.WIN_CLOSED:
        break
    print(values[0])

# Step 5: Close window
window.close()

