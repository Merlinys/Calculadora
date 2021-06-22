def resta():
    resta= input("""
Con x se termina de restar.
Ingrese el primer numero de la resta: """)
    if resta == "x":
        return "Nada calculado"
    resta = float(resta)
    print(resta)
    while True:
        num = input("""
Con x se termina la resta.
Ingrese el numero para restar: """)
        if num == "x":
            print("Resta finalizada")
            break
        num = float(num)
        resta -= num
        print(resta)


def sumar():
    suma =[]
    while True:
                num = input("""
Con x se termina de sumar.
Ingrese el numero de la suma: """)
                if num == "x":
                    return "Suma finalizada"
                num = float(num)
                suma.append(num)
                print(sum(suma))


def multiplicar():
    multi = input("""
Con x se termina la multiplicacion.
Ingrese el primer numero de la multiplicacion: """)
    if multi == "x":
            return "Nada calculado"
    multi = float(multi)
    while True:
        num = input("""
Con x se termina de multiplicar.
Ingrese para multiplicar: """)
        if num == "x":
            print("Multiplicacion finalizada")
            return False
        num = float(num)
        multi *= num
        print(multi)


def division(): 
    div = input("""
Con x se termina de dividir.
Ingrese el primer numero de la division: """)
    if div == "x":
        return "Nada calculado"
    div = float(div)
    print(div)
    while True:
        num = input("""
Con x se termina la division.
Ingrese el numero para dividir: """)
        if num == "x":
            print("Division finalizada")
            break
        num = float(num)
        div /= num
        print(div)


def run():
    numero = 0 
    while numero != 5:
        numero = int(input("""
Calculadora:
1.Sumar
2.Resta
3.Multiplicacion
4.Dividir
Elija otra numero para finalizar la operacion
Elija su operacion: """))
        if numero == 1:
            print(sumar())
        elif numero == 2:
            print(resta())
        elif numero == 3:
            print(multiplicar())
        elif numero == 4:
            print(division())
        else:
            print("Calculadora finalizada")
            return False


if __name__ == "__main__":
    run()
