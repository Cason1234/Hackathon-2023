import PySimpleGUI as pg

total_CO2 = 0


def oven(days, total_CO2):
    oven_CO2 = days * 52 * .28
    total_CO2 = total_CO2 + oven_CO2
    return total_CO2


def microwave(days, total_CO2):
    microwave_CO2 = days * 52 * .4
    total_CO2 = total_CO2 + microwave_CO2
    return total_CO2


def washing_machine(days, total_CO2):
    washing_machine_CO2 = days * 52 * .27
    total_CO2 = total_CO2 + washing_machine_CO2
    return total_CO2


def electric_oven(days, total_CO2):
    elec_oven_CO2 = days * 52 * .67
    total_CO2 = total_CO2 + elec_oven_CO2
    return total_CO2


def dishwasher(days, total_CO2):
    dishwasher_CO2 = days * 52 * .62
    total_CO2 = total_CO2 + dishwasher_CO2
    return total_CO2


# Step 1: Set theme
pg.theme("DarkAmber")

# Step 2: Create Layout
layout = [
    [pg.Text("How many times do you use your oven a week:", size=(46, 1)), pg.InputText(key='-oven-')],
    [pg.Text("How many times do you use your microwave a week: ", size=(46, 1)), pg.InputText(key='-microwave-')],
    [pg.Text("How many times do you use your washing machine a week: ", size=(46, 1)), pg.InputText(key='-washing-')],
    [pg.Text("How many times do you use your electric oven a week: ", size=(46, 1)), pg.InputText(key='-electric-')],
    [pg.Text("How many times do you use your dish washer a week: ", size=(46, 1)), pg.InputText(key='-dish-')],
    [pg.Button("Submit"), pg.Button("", key='value', visible=False)]
]

# Step 3: Create Window
window = pg.Window("Carbon Footprint Calculator", layout)

# Step 4: Event loop
while True:
    event, values = window.read()
    if event == pg.WIN_CLOSED:
        break
    if event == "Submit":
        total_CO2 = 0
        total_CO2 = oven(float(values['-oven-']), total_CO2)
        total_CO2 = microwave(float(values['-microwave-']), total_CO2)
        total_CO2 = washing_machine(float(values['-washing-']), total_CO2)
        total_CO2 = electric_oven(float(values['-electric-']), total_CO2)
        total_CO2 = dishwasher(float(values['-dish-']), total_CO2)
        total_CO2 = round(total_CO2, 3)
        window['value'].update(text=f'{total_CO2}kg is your Carbon Footprint', visible=True)
        #pg.Button()

    if event == "Microwave":
        window.close()
        layout = [
            [pg.Text("Times used per week: "), pg.InputText()],
            [pg.Button("Submit")]
        ]
        window = pg.Window("Times", layout)
        #event, values = window.read()






    #print(values[0])

# Step 5: Close window
window.close()

