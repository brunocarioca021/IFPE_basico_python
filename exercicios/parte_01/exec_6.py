#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salarioHora = float(input("Informe quanto você ganha por hora: "))

horasTrabalhadasMes = float(input("Informe quantas horas trabalhou no mês: "))

salarioTotal = salarioHora * horasTrabalhadasMes

print(f"Ganhos por hora {salarioHora:.2f} e ganhos por horas trabalhadas{horasTrabalhadasMes} hora do mês.")