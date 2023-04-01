import PySimpleGUI as pg


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


def main():
    return 0
