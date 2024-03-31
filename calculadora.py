x = 0.0
memory = []
while isinstance(x, float):
    x = input('Introduce un valor o signo')
    try:
        x = float(x)
        memory.append(x)
    except:
        if x == '+':
            print(f'El resultado de la suma es {sum(memory)}')
        elif x == '*':
            result = 1
            for value in memory:
                result = result * value
            print(f'El resultado de la multiplicación es {result}')
        elif x == '/':
            result = memory[0] ** 2
            for value in memory:
                result = result / value
            print(f'El resultado de la división es {result}')
        elif x == '%':
            if len(memory) == 2:
                print(f'El módulo es {int(memory[0] % memory[1])}')
            else:
                print('El operador módulo solo admite 2 valores')
        else:
            print('Hemos terminado')