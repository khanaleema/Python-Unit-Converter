def convert_units(category, from_unit, to_unit, value):
    if category == "Length":
        factors = {"Meter": 1, "Kilometer": 1000, "Centimeter": 0.01, "Mile": 1609.34}
        return round((value * factors[from_unit]) / factors[to_unit], 4)
    elif category == "Weight":
        factors = {"Kilogram": 1, "Gram": 0.001, "Pound": 0.453592, "Ounce": 0.0283495}
        return round((value * factors[from_unit]) / factors[to_unit], 4)
    elif category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return round((value * 9/5) + 32, 2)
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return round((value - 32) * 5/9, 2)
        else:
            return value
    elif category == "Speed":
        factors = {"m/s": 1, "km/h": 3.6, "mph": 2.23694}
        return round((value * factors[from_unit]) / factors[to_unit], 4)
    return None
