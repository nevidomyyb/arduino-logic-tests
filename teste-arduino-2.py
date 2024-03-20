# Dado que sensorValor é uma variável que armazena a leitura de um sensor de luminosidade, escreva uma condição que verifica se sensorValor está entre 400 e 600.

#Admitindo que o valor do sensorValor será recebido pelo sensor, mas nesse caso (em python) será apenas um input no terminal.
sensorValor = "A"
while type(sensorValor) is not float:
    try:
        sensorValor = float(input(""))
    except:
        print("Valor não aceitável, insira um valor númerico")
        sensorValor = "A"
if sensorValor >= 400 and sensorValor <= 600:
    print("O sensor detectou que o valor de luminosidade está entre 400 e 600")
    print(f"Valor do sensor: {sensorValor}")
