s = int(input("Digite quantos segundos: "))

horas = s // 3600
resto = s % 3600
minutos = resto // 60
segundos = resto % 60

print(horas,"horas",minutos,"minutos e",segundos,"segundos.")
