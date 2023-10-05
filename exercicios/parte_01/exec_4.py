#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

pi = 3.14159256
raio = float(input("Informe o raio do círculo: "))
area = pi * (raio ** 2)
print(f"O raio de um círculo {raio} é {area:.2f}m².")