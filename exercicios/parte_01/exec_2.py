#Faça um Programa que peça as 4 notas bimestrais e mostre a média
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
nota3 = float(input('Digite a nota 3: '))
nota4 = float(input('Digite a nota 4: '))

media = (nota1 + nota2 + nota3 + nota4)/4

print(f"A media das seguintes notas foram: Nota 1: {nota1:.2f}, Nota 2: {nota2:.2f}, Nota 3: {nota3:.2f}, Nota 4: {nota4:.2f}, Total da Média: {media:.2f}")