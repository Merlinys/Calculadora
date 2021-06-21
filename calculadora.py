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
Con x se termina de sumar.
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
    multi= input("""
Con x se termina de multiplicar.
Ingrese el primer numero de la resta: """)
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
    pass


def run():
    numero = 0 
    while numero != 5:
        numero = int(input("""
Calculadora:
1.Sumar
2.Resta
3.Multiplicacion
4.Dividir
5.Terminar calculadora
Elija su operacion: """))
        if numero == 1:
            print(sumar())
        elif numero == 2:
            print(resta())
        elif numero == 3:
            print(multiplicar())
        if numero == 4:
            pass
            


if __name__ == "__main__":
    run()
