def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32)/1.8

print("Insira a temperatura em °C para ser transformada em °F:")
celsius = float(input())
c_to_f = celsius_to_fahrenheit(celsius)

print("Insira a temperatura em °F para ser transformada em °C:")
fahrenheit = float(input())
f_to_c = fahrenheit_to_celsius(fahrenheit)

print(f"A temperatura {celsius}°C em Fahrenheit será {c_to_f} °F")
print(f"A temperatura {fahrenheit}°F em Celsius será {f_to_c} °C")