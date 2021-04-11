s = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = s // (3600*24)
resto = s % (3600*24)
horas = resto // 3600
resto2 = s % 3600
minutos = resto2 // 60
segundos = resto2 % 60

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")
