def resta():
    resta= input("""
Con x se termina de sumar.
Ingrese el numero de la suma: """)
    if resta == "x":
        print("Suma terminada")
    resta = int(resta)
    print(resta)
    while True:
        num = input("""
Con x se termina de sumar.
Ingrese el numero de la suma: """)
        if num == "x":
            print("Suma terminada")
            break
        num = int(num)
        resta -= num
        print(resta)

def sumar(suma):
    suma =[]
    while True:
                num = input("""
Con x se termina de sumar.
Ingrese el numero de la suma: """)
                if num == "x":
                    print("Suma terminada")
                    break
                num = int(num)
                suma.append(num)
                print(sum(suma))

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
            pass
            


if __name__ == "__main__":
    run()
