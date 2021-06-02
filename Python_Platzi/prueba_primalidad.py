def es_primo(numero):
    contador = True
    
    for i in range(1, numero+1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador = False
            break
    return contador

def run():
    numero = int(input("Escribe un numero:"))
    if es_primo(numero):
        print("Es primo")
    else:
        print("No es primo")

if __name__ == "__main__":
    run()