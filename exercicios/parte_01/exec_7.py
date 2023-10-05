#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).

grausFarenheit = float(input("Informe a tramperatura em Farenheit: "))

grausCelsius = 5*(grausFarenheit - 32) / 9

print(f"{grausFarenheit:.2f} graus Farenheit e {grausCelsius:.2f} graus Celsius")
