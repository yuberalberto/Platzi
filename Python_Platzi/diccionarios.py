def run():
    mi_diccionario = {
        "llave1": 1,
        "llave2": 2,
        "llave3": 3,
    }

    # print(mi_diccionario)

    poblacion_paises = {
        "Argentina": 44938712,
        "Colombia": 50372424,
        "Brasil": 210147125
    }

    # for pais in poblacion_paises.keys():
    #     print(pais)

    for pais, poblacion in poblacion_paises.items():
        print(pais + " tiene " + str(poblacion) + " Habitantes")

if __name__ == '__main__':
    run()