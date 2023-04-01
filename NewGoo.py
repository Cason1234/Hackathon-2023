import PySimpleGUI as pg

pg.theme("Dark Amber")

layout = [
    [pg.Button("Add Element")]
]

window = pg.Window("Carbon Footprint Calculator", layout)

while True:
    event, values = window.read()
    if event == pg.WIN_CLOSED:
        break
    if event == "Add Element":
        list_layout = [
            [pg.Button("Oven")],
            [pg.Button("Microwave")],
            [pg.Button("Washing Machine")],
            [pg.Button("Electric Oven")],
            [pg.Button("Dishwasher")]
        ]
        window = pg.Window("Options", list_layout)
        event, values = window.read()
        if event == "Oven":
            window.close()
            time_layout = [
                [pg.Text("Number of uses per week: "), pg.InputText()]
            ]
            window = pg.Window("Times", time_layout)
            event, values = window.read()

    #print(values[0])

# Step 5: Close window
window.close()