def divisor(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def main():
    
    while True:
        try:
            num = int(input("Enter a number: "))

            if num < 0:
                raise ValueError

            print(divisor(num))
            print("The End")

        except ValueError:
            print("Debes ingresar un numero positivo")

if __name__ == "__main__":
    main()