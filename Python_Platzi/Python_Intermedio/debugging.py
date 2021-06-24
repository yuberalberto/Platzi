def divisor(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def main():
    num = int(input("Enter a number: "))
    print(divisor(num))
    print("The End")

if __name__ == "__main__":
    main()