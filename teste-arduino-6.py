def is_number(string: str):
    try: 
        float(string)
        return True
    except:
        return False

operations = ""
currently_operation = "+"
while currently_operation != "=":
    if is_number(currently_operation):
        print("Digite uma operação:")
        print("+ adição | - subtração | * multiplicação | / divisão | = resultado")
    elif currently_operation in '+-*/':
        print("Digite um valor (para valores decimais utilize .)")
    currently_operation = input("")
    if currently_operation == "=": break
    if currently_operation not in '+-*/=':
        try:
            n = float(currently_operation)
        except:
            currently_operation = "+"
            continue
    operations += currently_operation

print(f"{operations} = {eval(operations)}")