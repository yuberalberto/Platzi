def run():
    nombre = input("Escribe tu nombre: ")
    print("La longitud del nombre es: "+str(len(nombre)))
    for letra in nombre:
        print(letra)


if __name__ == '__main__':
    run()