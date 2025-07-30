# Funções de conversão

def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_para_kelvin(c):
    return c + 273.15

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_para_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_para_celsius(k):
    return k - 273.15

def kelvin_para_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

# Solicita os dados do usuário
temperatura = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C, F, K): ").strip().upper()
destino = input("Unidade de destino (C, F, K): ").strip().upper()

# Conversão baseada na entrada
resultado = None

if origem == destino:
    resultado = temperatura
elif origem == "C" and destino == "F":
    resultado = celsius_para_fahrenheit(temperatura)
elif origem == "C" and destino == "K":
    resultado = celsius_para_kelvin(temperatura)
elif origem == "F" and destino == "C":
    resultado = fahrenheit_para_celsius(temperatura)
elif origem == "F" and destino == "K":
    resultado = fahrenheit_para_kelvin(temperatura)
elif origem == "K" and destino == "C":
    resultado = kelvin_para_celsius(temperatura)
elif origem == "K" and destino == "F":
    resultado = kelvin_para_fahrenheit(temperatura)
else:
    print("Unidade inválida.")

# Exibe o resultado, se houver
if  resultado is not None:
    print(f"\n{temperatura:.2f}°{origem} é igual a {resultado:.2f}°{destino}")
