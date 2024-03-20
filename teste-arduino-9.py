array = []
x = "A"

while x != "":
    print("Digite o valor da humidade, pressione Enter sem nada para parar a operação\n")
    x = input()
    try:
        value = float(x)
        array.append(value)
    except:
        continue
print(f"Max: {max(array)}")
print(f"Min: {min(array)}")
print(f"Média: {sum(array)/len(array)}")


