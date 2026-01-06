#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("╔════════════════════════════════════════════════════════╗")
print("║           🔄 UNIVERSAL UNIT CONVERTER 🔄               ║")
print("╚════════════════════════════════════════════════════════╝")

CATEGORIES = [
    "Length",
    "Weight/Mass",
    "Temperature",
    "Time",
    "Area",
    "Volume",
    "Speed",
    "Data/Storage"
]

for i, cat in enumerate(CATEGORIES, 1):
    print(f"  {i}. {cat}")


# In[ ]:


LENGTH_UNITS = {
    'meter': 1,
    'kilometer': 1000,
    'centimeter': 0.01,
    'millimeter': 0.001,
    'mile': 1609.344,
    'yard': 0.9144,
    'foot': 0.3048,
    'inch': 0.0254,
    'nautical_mile': 1852
}

print("📏 LENGTH UNITS:")
print("-" * 40)
for unit, factor in LENGTH_UNITS.items():
    print(f"  {unit:15} = {factor} meters")


# In[ ]:


def convert_length(value, from_unit, to_unit):
    """Convert length from one unit to another"""

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit not in LENGTH_UNITS:
        return f"Error: Unknown unit '{from_unit}'"
    if to_unit not in LENGTH_UNITS:
        return f"Error: Unknown unit '{to_unit}'"

    meters = value * LENGTH_UNITS[from_unit]
    result = meters / LENGTH_UNITS[to_unit]

    return result

print("📏 LENGTH CONVERSION TESTS:")
print(f"  5 kilometers = {convert_length(5, 'kilometer', 'mile'):.4f} miles")
print(f"  100 meters = {convert_length(100, 'meter', 'foot'):.4f} feet")
print(f"  12 inches = {convert_length(12, 'inch', 'centimeter'):.4f} centimeters")
print(f"  1 mile = {convert_length(1, 'mile', 'kilometer'):.4f} kilometers")


# In[ ]:


WEIGHT_UNITS = {
    'kilogram': 1,
    'gram': 0.001,
    'milligram': 0.000001,
    'metric_ton': 1000,
    'pound': 0.453592,
    'ounce': 0.0283495,
    'stone': 6.35029,
    'carat': 0.0002
}

print("⚖️ WEIGHT/MASS UNITS:")
print("-" * 40)
for unit, factor in WEIGHT_UNITS.items():
    print(f"  {unit:15} = {factor} kilograms")


# In[ ]:


def convert_weight(value, from_unit, to_unit):
    """Convert weight from one unit to another"""

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit not in WEIGHT_UNITS:
        return f"Error: Unknown unit '{from_unit}'"
    if to_unit not in WEIGHT_UNITS:
        return f"Error: Unknown unit '{to_unit}'"

    kilograms = value * WEIGHT_UNITS[from_unit]
    result = kilograms / WEIGHT_UNITS[to_unit]

    return result

print("⚖️ WEIGHT CONVERSION TESTS:")
print(f"  10 kilograms = {convert_weight(10, 'kilogram', 'pound'):.4f} pounds")
print(f"  500 grams = {convert_weight(500, 'gram', 'ounce'):.4f} ounces")
print(f"  150 pounds = {convert_weight(150, 'pound', 'kilogram'):.4f} kilograms")
print(f"  1 metric_ton = {convert_weight(1, 'metric_ton', 'pound'):.4f} pounds")


# In[ ]:


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

print("🌡️ TEMPERATURE CONVERSION TESTS:")
print(f"  0°C = {celsius_to_fahrenheit(0):.2f}°F")
print(f"  100°C = {celsius_to_fahrenheit(100):.2f}°F")
print(f"  32°F = {fahrenheit_to_celsius(32):.2f}°C")
print(f"  98.6°F = {fahrenheit_to_celsius(98.6):.2f}°C")
print(f"  0°C = {celsius_to_kelvin(0):.2f}K")
print(f"  273.15K = {kelvin_to_celsius(273.15):.2f}°C")


# In[ ]:


def convert_temperature(value, from_unit, to_unit):
    """Convert temperature from one unit to another"""

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    unit_map = {
        'c': 'celsius', 'celsius': 'celsius',
        'f': 'fahrenheit', 'fahrenheit': 'fahrenheit',
        'k': 'kelvin', 'kelvin': 'kelvin'
    }

    from_unit = unit_map.get(from_unit, from_unit)
    to_unit = unit_map.get(to_unit, to_unit)

    if from_unit == to_unit:
        return value

    conversions = {
        ('celsius', 'fahrenheit'): celsius_to_fahrenheit,
        ('fahrenheit', 'celsius'): fahrenheit_to_celsius,
        ('celsius', 'kelvin'): celsius_to_kelvin,
        ('kelvin', 'celsius'): kelvin_to_celsius,
        ('fahrenheit', 'kelvin'): fahrenheit_to_kelvin,
        ('kelvin', 'fahrenheit'): kelvin_to_fahrenheit
    }

    converter = conversions.get((from_unit, to_unit))
    if converter:
        return converter(value)
    else:
        return "Error: Invalid conversion"

print("🌡️ TEMPERATURE CONVERSIONS:")
print(f"  25°C = {convert_temperature(25, 'C', 'F'):.2f}°F")
print(f"  77°F = {convert_temperature(77, 'F', 'C'):.2f}°C")
print(f"  300K = {convert_temperature(300, 'K', 'C'):.2f}°C")


# In[ ]:


TIME_UNITS = {
    'second': 1,
    'millisecond': 0.001,
    'microsecond': 0.000001,
    'nanosecond': 0.000000001,
    'minute': 60,
    'hour': 3600,
    'day': 86400,
    'week': 604800,
    'month': 2592000,
    'year': 31536000
}

print("⏰ TIME UNITS:")
print("-" * 40)
for unit, factor in TIME_UNITS.items():
    print(f"  {unit:15} = {factor} seconds")


# In[ ]:


def convert_time(value, from_unit, to_unit):
    """Convert time from one unit to another"""

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit not in TIME_UNITS:
        return f"Error: Unknown unit '{from_unit}'"
    if to_unit not in TIME_UNITS:
        return f"Error: Unknown unit '{to_unit}'"

    seconds = value * TIME_UNITS[from_unit]
    result = seconds / TIME_UNITS[to_unit]

    return result

print("⏰ TIME CONVERSION TESTS:")
print(f"  2 hours = {convert_time(2, 'hour', 'minute'):.2f} minutes")
print(f"  1 day = {convert_time(1, 'day', 'hour'):.2f} hours")
print(f"  1 week = {convert_time(1, 'week', 'day'):.2f} days")
print(f"  365 days = {convert_time(365, 'day', 'year'):.4f} years")
print(f"  1000 milliseconds = {convert_time(1000, 'millisecond', 'second'):.2f} seconds")


# In[ ]:


AREA_UNITS = {
    'square_meter': 1,
    'square_kilometer': 1000000,
    'square_centimeter': 0.0001,
    'square_millimeter': 0.000001,
    'hectare': 10000,
    'acre': 4046.8564224,
    'square_foot': 0.09290304,
    'square_yard': 0.83612736,
    'square_inch': 0.00064516,
    'square_mile': 2589988.110336
}

print("📐 AREA UNITS:")
print("-" * 50)
for unit, factor in AREA_UNITS.items():
    print(f"  {unit:20} = {factor} m²")


# In[ ]:


def convert_area(value, from_unit, to_unit):
    """Convert area from one unit to another"""

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit not in AREA_UNITS:
        return f"Error: Unknown unit '{from_unit}'"
    if to_unit not in AREA_UNITS:
        return f"Error: Unknown unit '{to_unit}'"

    sq_meters = value * AREA_UNITS[from_unit]
    result = sq_meters / AREA_UNITS[to_unit]

    return result

print("📐 AREA CONVERSION TESTS:")
print(f"  1 hectare = {convert_area(1, 'hectare', 'acre'):.4f} acres")
print(f"  100 square_foot = {convert_area(100, 'square_foot', 'square_meter'):.4f} m²")
print(f"  1 square_kilometer = {convert_area(1, 'square_kilometer', 'hectare'):.2f} hectares")
print(f"  1 acre = {convert_area(1, 'acre', 'square_foot'):.2f} sq feet")


# In[ ]:


VOLUME_UNITS = {
    'liter': 1,
    'milliliter': 0.001,
    'cubic_meter': 1000,
    'cubic_centimeter': 0.001,
    'gallon_us': 3.78541,
    'gallon_uk': 4.54609,
    'quart': 0.946353,
    'pint': 0.473176,
    'cup': 0.236588,
    'fluid_ounce': 0.0295735,
    'tablespoon': 0.0147868,
    'teaspoon': 0.00492892
}

print("🧪 VOLUME UNITS:")
print("-" * 50)
for unit, factor in VOLUME_UNITS.items():
    print(f"  {unit:20} = {factor} liters")


# In[ ]:


def convert_volume(value, from_unit, to_unit):
    """Convert volume from one unit to another"""

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit not in VOLUME_UNITS:
        return f"Error: Unknown unit '{from_unit}'"
    if to_unit not in VOLUME_UNITS:
        return f"Error: Unknown unit '{to_unit}'"

    liters = value * VOLUME_UNITS[from_unit]
    result = liters / VOLUME_UNITS[to_unit]

    return result

print("🧪 VOLUME CONVERSION TESTS:")
print(f"  1 gallon_us = {convert_volume(1, 'gallon_us', 'liter'):.4f} liters")
print(f"  500 milliliter = {convert_volume(500, 'milliliter', 'cup'):.4f} cups")
print(f"  1 liter = {convert_volume(1, 'liter', 'fluid_ounce'):.4f} fluid ounces")
print(f"  1 tablespoon = {convert_volume(1, 'tablespoon', 'teaspoon'):.2f} teaspoons")


# In[ ]:


SPEED_UNITS = {
    'meter_per_second': 1,
    'kilometer_per_hour': 0.277778,
    'mile_per_hour': 0.44704,
    'foot_per_second': 0.3048,
    'knot': 0.514444,
    'mach': 343
}

print("🚗 SPEED UNITS:")
print("-" * 50)
for unit, factor in SPEED_UNITS.items():
    print(f"  {unit:20} = {factor} m/s")


# In[ ]:


def convert_speed(value, from_unit, to_unit):
    """Convert speed from one unit to another"""

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit not in SPEED_UNITS:
        return f"Error: Unknown unit '{from_unit}'"
    if to_unit not in SPEED_UNITS:
        return f"Error: Unknown unit '{to_unit}'"

    mps = value * SPEED_UNITS[from_unit]
    result = mps / SPEED_UNITS[to_unit]

    return result

print("🚗 SPEED CONVERSION TESTS:")
print(f"  100 km/h = {convert_speed(100, 'kilometer_per_hour', 'mile_per_hour'):.4f} mph")
print(f"  60 mph = {convert_speed(60, 'mile_per_hour', 'kilometer_per_hour'):.4f} km/h")
print(f"  1 mach = {convert_speed(1, 'mach', 'kilometer_per_hour'):.2f} km/h")
print(f"  50 knot = {convert_speed(50, 'knot', 'kilometer_per_hour'):.4f} km/h")


# In[ ]:


DATA_UNITS = {
    'bit': 0.125,
    'byte': 1,
    'kilobyte': 1024,
    'megabyte': 1024 ** 2,
    'gigabyte': 1024 ** 3,
    'terabyte': 1024 ** 4,
    'petabyte': 1024 ** 5,
    'kibibyte': 1024,
    'mebibyte': 1024 ** 2,
    'gibibyte': 1024 ** 3
}

print("💾 DATA/STORAGE UNITS:")
print("-" * 50)
for unit, factor in DATA_UNITS.items():
    print(f"  {unit:15} = {factor:,.0f} bytes")


# In[ ]:


def convert_data(value, from_unit, to_unit):
    """Convert data size from one unit to another"""

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit not in DATA_UNITS:
        return f"Error: Unknown unit '{from_unit}'"
    if to_unit not in DATA_UNITS:
        return f"Error: Unknown unit '{to_unit}'"

    bytes_val = value * DATA_UNITS[from_unit]
    result = bytes_val / DATA_UNITS[to_unit]

    return result

print("💾 DATA CONVERSION TESTS:")
print(f"  1 gigabyte = {convert_data(1, 'gigabyte', 'megabyte'):.2f} megabytes")
print(f"  1024 megabyte = {convert_data(1024, 'megabyte', 'gigabyte'):.2f} gigabytes")
print(f"  1 terabyte = {convert_data(1, 'terabyte', 'gigabyte'):.2f} gigabytes")
print(f"  8 bit = {convert_data(8, 'bit', 'byte'):.2f} bytes")
print(f"  500 gigabyte = {convert_data(500, 'gigabyte', 'terabyte'):.4f} terabytes")


# In[ ]:


class UnitConverter:
    def __init__(self):
        self.length = LENGTH_UNITS
        self.weight = WEIGHT_UNITS
        self.time = TIME_UNITS
        self.area = AREA_UNITS
        self.volume = VOLUME_UNITS
        self.speed = SPEED_UNITS
        self.data = DATA_UNITS

    def convert(self, value, from_unit, to_unit, category):
        """Universal conversion method"""

        category = category.lower()
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        units_dict = {
            'length': self.length,
            'weight': self.weight,
            'time': self.time,
            'area': self.area,
            'volume': self.volume,
            'speed': self.speed,
            'data': self.data
        }

        if category not in units_dict:
            return f"Error: Unknown category '{category}'"

        units = units_dict[category]

        if from_unit not in units:
            return f"Error: Unknown unit '{from_unit}'"
        if to_unit not in units:
            return f"Error: Unknown unit '{to_unit}'"

        base_value = value * units[from_unit]
        result = base_value / units[to_unit]

        return result

    def list_units(self, category):
        """List all units in a category"""
        category = category.lower()
        units_dict = {
            'length': self.length,
            'weight': self.weight,
            'time': self.time,
            'area': self.area,
            'volume': self.volume,
            'speed': self.speed,
            'data': self.data
        }

        if category in units_dict:
            return list(units_dict[category].keys())
        return []

converter = UnitConverter()

print("🔄 UNIVERSAL CONVERTER TESTS:")
print(f"  5 km to miles: {converter.convert(5, 'kilometer', 'mile', 'length'):.4f}")
print(f"  10 kg to pounds: {converter.convert(10, 'kilogram', 'pound', 'weight'):.4f}")
print(f"  2 hours to minutes: {converter.convert(2, 'hour', 'minute', 'time'):.2f}")


# In[ ]:


km_to_miles = lambda km: km * 0.621371
miles_to_km = lambda miles: miles * 1.60934
feet_to_meters = lambda feet: feet * 0.3048
meters_to_feet = lambda meters: meters * 3.28084

kg_to_pounds = lambda kg: kg * 2.20462
pounds_to_kg = lambda lb: lb * 0.453592

c_to_f = lambda c: (c * 9/5) + 32
f_to_c = lambda f: (f - 32) * 5/9

print("⚡ QUICK CONVERSIONS:")
print(f"  10 km = {km_to_miles(10):.2f} miles")
print(f"  5 miles = {miles_to_km(5):.2f} km")
print(f"  70 kg = {kg_to_pounds(70):.2f} pounds")
print(f"  37°C = {c_to_f(37):.2f}°F")


# In[ ]:


def generate_conversion_table(category, unit, values):
    """Generate a conversion table for given values"""

    units_dict = {
        'length': LENGTH_UNITS,
        'weight': WEIGHT_UNITS,
        'time': TIME_UNITS,
        'area': AREA_UNITS,
        'volume': VOLUME_UNITS,
        'speed': SPEED_UNITS,
        'data': DATA_UNITS
    }

    if category not in units_dict:
        print(f"Error: Unknown category '{category}'")
        return

    units = units_dict[category]

    if unit not in units:
        print(f"Error: Unknown unit '{unit}'")
        return

    print(f"\n📊 CONVERSION TABLE: {unit.upper()}")
    print("=" * 80)

    other_units = [u for u in units.keys() if u != unit][:5]
    header = f"{'Value':>10} |"
    for u in other_units:
        header += f" {u:>12} |"
    print(header)
    print("-" * 80)

    for val in values:
        row = f"{val:>10} |"
        for u in other_units:
            converted = (val * units[unit]) / units[u]
            row += f" {converted:>12.4f} |"
        print(row)

generate_conversion_table('length', 'kilometer', [1, 5, 10, 50, 100])


# In[ ]:


def show_menu():
    print("\n" + "=" * 50)
    print("🔄 UNIT CONVERTER - MAIN MENU")
    print("=" * 50)
    print("1. 📏 Length Conversion")
    print("2. ⚖️  Weight/Mass Conversion")
    print("3. 🌡️  Temperature Conversion")
    print("4. ⏰ Time Conversion")
    print("5. 📐 Area Conversion")
    print("6. 🧪 Volume Conversion")
    print("7. 🚗 Speed Conversion")
    print("8. 💾 Data/Storage Conversion")
    print("9. 📊 Generate Conversion Table")
    print("0. ❌ Exit")
    print("=" * 50)

def get_available_units(category):
    """Get available units for a category"""
    units_map = {
        '1': ('length', LENGTH_UNITS),
        '2': ('weight', WEIGHT_UNITS),
        '3': ('temperature', ['celsius', 'fahrenheit', 'kelvin']),
        '4': ('time', TIME_UNITS),
        '5': ('area', AREA_UNITS),
        '6': ('volume', VOLUME_UNITS),
        '7': ('speed', SPEED_UNITS),
        '8': ('data', DATA_UNITS)
    }
    return units_map.get(category, (None, None))

show_menu()


# In[ ]:


def run_converter():
    converter = UnitConverter()

    while True:
        show_menu()
        choice = input("\n👉 Enter your choice (0-9): ")

        if choice == '0':
            print("\n👋 Thank you for using Unit Converter! Goodbye!")
            break

        elif choice in ['1', '2', '4', '5', '6', '7', '8']:
            category_name, units = get_available_units(choice)

            if isinstance(units, dict):
                unit_list = list(units.keys())
            else:
                unit_list = units

            print(f"\n📋 Available {category_name.upper()} units:")
            for i, unit in enumerate(unit_list, 1):
                print(f"   {i}. {unit}")

            try:
                value = float(input("\n📝 Enter value to convert: "))
                from_unit = input("📝 Enter source unit: ").lower()
                to_unit = input("📝 Enter target unit: ").lower()

                if category_name == 'length':
                    result = convert_length(value, from_unit, to_unit)
                elif category_name == 'weight':
                    result = convert_weight(value, from_unit, to_unit)
                elif category_name == 'time':
                    result = convert_time(value, from_unit, to_unit)
                elif category_name == 'area':
                    result = convert_area(value, from_unit, to_unit)
                elif category_name == 'volume':
                    result = convert_volume(value, from_unit, to_unit)
                elif category_name == 'speed':
                    result = convert_speed(value, from_unit, to_unit)
                elif category_name == 'data':
                    result = convert_data(value, from_unit, to_unit)

                print(f"\n✅ RESULT: {value} {from_unit} = {result:.6f} {to_unit}")

            except ValueError:
                print("❌ Invalid input! Please enter a valid number.")

        elif choice == '3':
            print("\n🌡️ TEMPERATURE CONVERSION")
            print("   Units: celsius (C), fahrenheit (F), kelvin (K)")

            try:
                value = float(input("\n📝 Enter temperature value: "))
                from_unit = input("📝 Enter source unit (C/F/K): ")
                to_unit = input("📝 Enter target unit (C/F/K): ")

                result = convert_temperature(value, from_unit, to_unit)
                print(f"\n✅ RESULT: {value}° {from_unit.upper()} = {result:.2f}° {to_unit.upper()}")

            except ValueError:
                print("❌ Invalid input! Please enter a valid number.")

        elif choice == '9':
            print("\n📊 GENERATE CONVERSION TABLE")
            print("Categories: length, weight, time, area, volume, speed, data")

            category = input("📝 Enter category: ").lower()
            unit = input("📝 Enter base unit: ").lower()

            values = [1, 5, 10, 25, 50, 100]
            generate_conversion_table(category, unit, values)

        else:
            print("❌ Invalid choice! Please try again.")

        input("\n⏎ Press Enter to continue...")

print("✅ Interactive converter ready! Call run_converter() to start.")


# In[ ]:


def batch_convert(values_list, from_unit, to_unit, category):
    """Convert multiple values at once"""

    conversion_func = {
        'length': convert_length,
        'weight': convert_weight,
        'time': convert_time,
        'area': convert_area,
        'volume': convert_volume,
        'speed': convert_speed,
        'data': convert_data
    }

    if category not in conversion_func:
        return "Error: Unknown category"

    results = []
    func = conversion_func[category]

    for value in values_list:
        result = func(value, from_unit, to_unit)
        results.append((value, result))

    return results

values = [1, 5, 10, 25, 50, 100]
results = batch_convert(values, 'kilometer', 'mile', 'length')

print("📊 BATCH CONVERSION: Kilometers to Miles")
print("-" * 40)
for km, miles in results:
    print(f"   {km:>6} km = {miles:>10.4f} miles")


# In[ ]:


import matplotlib.pyplot as plt

def visualize_conversion(from_values, from_unit, to_unit, category):
    """Create a visual chart for conversions"""

    results = batch_convert(from_values, from_unit, to_unit, category)

    from_vals = [r[0] for r in results]
    to_vals = [r[1] for r in results]

    fig, ax = plt.subplots(figsize=(10, 6))

    bars = ax.bar(range(len(from_vals)), to_vals, color='steelblue', edgecolor='black')

    ax.set_xlabel(f'{from_unit}', fontsize=12)
    ax.set_ylabel(f'{to_unit}', fontsize=12)
    ax.set_title(f'Conversion: {from_unit} → {to_unit}', fontsize=14, fontweight='bold')
    ax.set_xticks(range(len(from_vals)))
    ax.set_xticklabels([str(v) for v in from_vals])

    for bar, val in zip(bars, to_vals):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f'{val:.2f}', ha='center', fontsize=10)

    plt.tight_layout()
    plt.show()

print("📊 Visualization function ready! Call visualize_conversion() to use.")


# In[ ]:


import csv

def export_to_csv(category, from_unit, values, filename='conversion_table.csv'):
    """Export conversion table to CSV file"""

    units_dict = {
        'length': LENGTH_UNITS,
        'weight': WEIGHT_UNITS,
        'time': TIME_UNITS,
        'area': AREA_UNITS,
        'volume': VOLUME_UNITS,
        'speed': SPEED_UNITS,
        'data': DATA_UNITS
    }

    if category not in units_dict:
        print(f"Error: Unknown category '{category}'")
        return

    units = units_dict[category]
    other_units = [u for u in units.keys() if u != from_unit]

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)

        header = [from_unit] + other_units
        writer.writerow(header)

        for val in values:
            row = [val]
            for u in other_units:
                converted = (val * units[from_unit]) / units[u]
                row.append(f"{converted:.6f}")
            writer.writerow(row)

    print(f"✅ Conversion table exported to '{filename}'")

export_to_csv('length', 'meter', [1, 10, 100, 1000], 'length_conversion.csv')


# In[ ]:


def convert(value, from_unit, to_unit):
    """
    Universal converter that auto-detects category
    """

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    all_units = {
        'length': LENGTH_UNITS,
        'weight': WEIGHT_UNITS,
        'time': TIME_UNITS,
        'area': AREA_UNITS,
        'volume': VOLUME_UNITS,
        'speed': SPEED_UNITS,
        'data': DATA_UNITS
    }

    detected_category = None
    for category, units in all_units.items():
        if from_unit in units and to_unit in units:
            detected_category = category
            break

    temp_units = ['celsius', 'fahrenheit', 'kelvin', 'c', 'f', 'k']
    if from_unit in temp_units and to_unit in temp_units:
        return convert_temperature(value, from_unit, to_unit)

    if detected_category is None:
        return "Error: Could not detect unit category or units are from different categories"

    units = all_units[detected_category]
    base_value = value * units[from_unit]
    result = base_value / units[to_unit]

    return result

print("🔄 UNIVERSAL CONVERTER TESTS:")
print(f"  10 km to miles: {convert(10, 'kilometer', 'mile'):.4f}")
print(f"  5 pounds to kg: {convert(5, 'pound', 'kilogram'):.4f}")
print(f"  100°C to °F: {convert(100, 'celsius', 'fahrenheit'):.2f}")
print(f"  3600 seconds to hours: {convert(3600, 'second', 'hour'):.2f}")
print(f"  1 GB to MB: {convert(1, 'gigabyte', 'megabyte'):.2f}")


# In[ ]:


def print_quick_reference():
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                        🔄 UNIT CONVERTER - QUICK REFERENCE                   ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  📏 LENGTH                      ⚖️ WEIGHT                                    ║
║  ─────────────────────          ─────────────────────                        ║
║  • 1 km = 0.6214 miles          • 1 kg = 2.2046 pounds                       ║
║  • 1 mile = 1.6093 km           • 1 pound = 0.4536 kg                        ║
║  • 1 inch = 2.54 cm             • 1 ounce = 28.35 grams                      ║
║  • 1 foot = 0.3048 m            • 1 stone = 6.35 kg                          ║
║                                                                              ║
║  🌡️ TEMPERATURE                 ⏰ TIME                                       ║
║  ─────────────────────          ─────────────────────                        ║
║  • °F = (°C × 9/5) + 32         • 1 hour = 60 minutes                        ║
║  • °C = (°F - 32) × 5/9         • 1 day = 24 hours                           ║
║  • K = °C + 273.15              • 1 week = 7 days                            ║
║                                                                              ║
║  💾 DATA                         🧪 VOLUME                                    ║
║  ─────────────────────          ─────────────────────                        ║
║  • 1 KB = 1024 bytes            • 1 liter = 1000 ml                          ║
║  • 1 MB = 1024 KB               • 1 gallon = 3.785 liters                    ║
║  • 1 GB = 1024 MB               • 1 cup = 236.6 ml                           ║
║  • 1 TB = 1024 GB               • 1 tablespoon = 14.8 ml                     ║
║                                                                              ║
║  🚗 SPEED                        📐 AREA                                      ║
║  ─────────────────────          ─────────────────────                        ║
║  • 1 km/h = 0.6214 mph          • 1 hectare = 2.471 acres                    ║
║  • 1 mph = 1.6093 km/h          • 1 acre = 43,560 sq ft                      ║
║  • 1 knot = 1.852 km/h          • 1 sq km = 100 hectares                     ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
""")

print_quick_reference()


# In[ ]:




