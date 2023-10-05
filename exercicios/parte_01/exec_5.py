#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

quadrado = float(input("Informe a área do quadrado: "))

area = quadrado ** 2
dobro = area * 2
print(f"O dobro da área do quadrado {quadrado:.2f}m é {dobro:.2f}m²") 