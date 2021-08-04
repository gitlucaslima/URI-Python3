valor = int(input())

horas = valor / 3600
restohoras = valor % 3600

minutos = restohoras / 60
restominutos = restohoras % 60

segundos = restominutos

print('{}:{}:{}'.format(int(horas), int(minutos), int(segundos)))
