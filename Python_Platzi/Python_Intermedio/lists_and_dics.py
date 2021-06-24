def main():
    my_list = [1, "Hello", True, 4.5]
    my_dic = {"firstname": "Facundo", "lastname": "Garcia"}

    super_list = [
        {"firstname": "Facundo", "lastname": "Garcia"},
        {"firstname": "Miguel", "lastname": "Torres"},
        {"firstname": "Pepe", "lastname": "Rodelo"},
        {"firstname": "Susana", "lastname": "Martinez"},
        {"firstname": "José", "lastname": "Garcia"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-2, -1, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)
    
    print("There are " + str(len(super_list)) + " dictionaries in the list super_list")
    
    for index in range(len(super_list)):
        print("Dict", index+1, "=>", super_list[index])

if __name__ == "__main__":
    main()