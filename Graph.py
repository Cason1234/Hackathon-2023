import PySimpleGUI as pg

total_CO2 = 0
def oven(days, total_CO2):
    oven_CO2 = days * 52 * .28
    total_CO2 = total_CO2 + oven_CO2
    return total_CO2

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
        window.close()
        list_layout = [
            [pg.Button("Oven")],
            [pg.Button("Microwave")],
            [pg.Button("Washing Machine")],
            [pg.Button("Electric Oven")],
            [pg.Button("Dishwasher")]
        ]
        window = pg.Window('Options For whatever', list_layout)
        event, values = window.read()
    if  event == "Oven":
        window.close()
        layout = [
            [pg.Text("Times used per week: "), pg.InputText()],
            [pg.Button("Submit")]
        ]
        window = pg.Window("Times", layout)
        event, values = window.read()
        if event == "Submit":
            time = float(values[0])
            total_CO2 = oven(time, total_CO2)
            window.close()
            list_layout = [
                [pg.Button("Oven")],
                [pg.Button("Microwave")],
                [pg.Button("Washing Machine")],
                [pg.Button("Electric Oven")],
                [pg.Button("Dishwasher")]
            ]
            window = pg.Window('Options For whatever', list_layout)
            event, values = window.read()
            if event == "Microwave":
                window.close()
                layout = [
                    [pg.Text("Times used per week: "), pg.InputText()],
                    [pg.Button("Submit")]
                ]
                window = pg.Window("Times", layout)
                event, values = window.read()






    #print(values[0])

# Step 5: Close window
window.close()

