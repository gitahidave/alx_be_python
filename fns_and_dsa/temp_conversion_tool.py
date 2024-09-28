# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_OFFSET = 32

def convert_to_celsius(fahrenheit):
    """
    Convert a temperature from Fahrenheit to Celsius using the global conversion factor.
    
    Parameters:
    fahrenheit (float): Temperature in Fahrenheit.
    
    Returns:
    float: Temperature in Celsius.
    """
    global FAHRENHEIT_TO_CELSIUS_FACTOR, FAHRENHEIT_OFFSET
    return (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert a temperature from Celsius to Fahrenheit using the global conversion factor.
    
    Parameters:
    celsius (float): Temperature in Celsius.
    
    Returns:
    float: Temperature in Fahrenheit.
    """
    global CELSIUS_TO_FAHRENHEIT_FACTOR, FAHRENHEIT_OFFSET
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + FAHRENHEIT_OFFSET

def main():
    try:
        # Prompt the user for input
        temp = input("Enter the temperature: ").strip()
        
        # Ensure the temperature is a numeric value
        temp = float(temp)
        
        # Prompt the user for the unit of temperature
        unit = input("Is the temperature in Celsius (C) or Fahrenheit (F)? ").strip().upper()

        # Convert based on the input unit
        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp}°C is equal to {converted_temp:.2f}°F.")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}°F is equal to {converted_temp:.2f}°C.")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
