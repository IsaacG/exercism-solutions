colors_resistors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

tolerances = {
    "grey": " ±0.05%",
    "violet": " ±0.1%",
    "blue": " ±0.25%",
    "green": " ±0.5%",
    "brown": " ±1%",
    "red": " ±2%",
    "gold": " ±5%",
    "silver": " ±10%"
}

def scale(resistor_value, multiply):
    print(f"scale({resistor_value}, {multiply})")
    if multiply <= 1:
        return f"{resistor_value} ohms"
    elif multiply >= 2 and multiply <= 5:
        result = resistor_value / 1000
        if result.is_integer():
            return f"{int(result)} kiloohms"
        else:
            return f"{result:.2f} kiloohms"  # Format to two decimal places
    elif multiply == 6 and resistor_value > 1000:
        return f"{resistor_value/1e6:.2f} megaohms"  # Format to two decimal places
    elif multiply == 9:
        return f"{resistor_value} gigaohms"
    else:
        return f"{resistor_value} ohms"

def listvalues(bands):
    values = []
    for color in bands:
        for idx, resistor in enumerate(colors_resistors):
            if resistor == color:
                values.append(str(idx))
    return values

def resistorInfo(values,multiply,tolerance):
    resistor_value = int("".join(values)) * (10 ** multiply)
    return scale(resistor_value, multiply) + tolerances[tolerance]

def resistor_label(colors):
    multiply = colors_resistors.index(colors[-2])
    tolerance = colors[-1]
    if len(colors) == 4:
        bands = colors[:2]
        values = listvalues(bands)
        return resistorInfo(values,multiply,tolerance)
    elif len(colors) == 5:
        bands = colors[:3]
        values = listvalues(bands)
        resistor_value = int("".join(values)) * (10 ** multiply)
        value = scale(resistor_value, multiply)
        result = scale(resistor_value, multiply) + tolerances[tolerance.lower()]
        return result
