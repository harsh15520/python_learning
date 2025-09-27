## 1. **Basic: Celsius to Fahrenheit**

```python
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius * 9/5 + 32
print(f"{celsius}°C = {fahrenheit}°F")
```
- **Formula:** $$ F = C \times \frac{9}{5} + 32 $$

***

## 2. **Intermediate: Celsius, Fahrenheit, Kelvin (Choose Direction)**

```python
def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

# Example usage:
choice = input("Convert from (C/F/K): ").strip().upper()
value = float(input("Enter the temperature value: "))

if choice == 'C':
    print(f"{value}°C = {celsius_to_fahrenheit(value):.2f}°F")
    print(f"{value}°C = {celsius_to_kelvin(value):.2f}K")
elif choice == 'F':
    c = fahrenheit_to_celsius(value)
    print(f"{value}°F = {c:.2f}°C")
    print(f"{value}°F = {celsius_to_kelvin(c):.2f}K")
elif choice == 'K':
    c = kelvin_to_celsius(value)
    print(f"{value}K = {c:.2f}°C")
    print(f"{value}K = {celsius_to_fahrenheit(c):.2f}°F")
else:
    print("Invalid unit.")
```

***

## 3. **Advanced: Universal Temperature Converter Function**

This function handles all conversions between Celsius, Fahrenheit, and Kelvin, using the correct formula for each case.
```python
def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """
    Converts a temperature from one unit to another.
    Args:
        value (float): The temperature value to convert.
        from_unit (str): 'C', 'F', or 'K'.
        to_unit (str): 'C', 'F', or 'K'.
    Returns:
        float: The converted temperature.
    Raises:
        ValueError: If an invalid unit is provided.
    """
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()
    if from_unit == to_unit:
        return value
    # Convert to Celsius as a base
    if from_unit == 'F':
        c = (value - 32) * 5/9
    elif from_unit == 'K':
        c = value - 273.15
    elif from_unit == 'C':
        c = value
    else:
        raise ValueError("Invalid from_unit")
    # Convert from Celsius to target
    if to_unit == 'C':
        return c
    elif to_unit == 'F':
        return c * 9/5 + 32
    elif to_unit == 'K':
        return c + 273.15
    else:
        raise ValueError("Invalid to_unit")

# Example usage:
try:
    val = float(input("Enter temperature value: "))
    from_u = input("From unit (C/F/K): ")
    to_u = input("To unit (C/F/K): ")
    result = convert_temperature(val, from_u, to_u)
    print(f"{val:.2f}°{from_u.upper()} = {result:.2f}°{to_u.upper()}")
except Exception as e:
    print(f"Error: {e}")
```

***

## 4. **Reference Table: Temperature Conversion Formulas**

| From | To | Formula |
|------|----|---------|
| C    | F  | $$ F = C \times \frac{9}{5} + 32 $$ |
| F    | C  | $$ C = (F - 32) \times \frac{5}{9} $$ |
| C    | K  | $$ K = C + 273.15 $$ |
| K    | C  | $$ C = K - 273.15 $$ |
| F    | K  | $$ K = (F - 32) \times \frac{5}{9} + 273.15 $$ |
| K    | F  | $$ F = (K - 273.15) \times \frac{9}{5} + 32 $$ |

***

## 5. **Practice Challenge**
- Try extending the advanced function to support batch conversions (a list of values).
- Add error handling for invalid input (non-numeric values, wrong units).
- Create a menu-driven app for repeated conversions.
