import random

def adivinador(numero_usuario, numero_secreto):
    if numero_usuario < numero_secreto:
        return "El numero es mayor"
    elif numero_usuario > numero_secreto:
        return "El numero es menor"
    else:
        return "Ganaste!"

def run():
    ns = int(random.randint(1, 100))
    resultado = ""
    while  resultado != "Ganaste!":
        nu = int(input("Adivina el numero entre 0 y 100: "))
        resultado = adivinador(nu, ns)
        print(resultado)
        if resultado == "Ganaste!":
            print("El número es "+str(nu))
            break

if __name__ == "__main__":
    run()