totalSegundos = int(input("Por favor, entre com o número de segundos que deseja converter:"))
dias = totalSegundos // 86400
horas = (totalSegundos % 86400) // 3600
minutos = ((totalSegundos % 86400) % 3600) // 60
segundos = ((totalSegundos % 86400) % 3600) % 60
print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")
