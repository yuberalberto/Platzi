def main():
    # list=[]
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         list.append(i**2)
    # print(list)

    
    # print([i**2 for i in range(1, 101) if i % 3 != 0]) #comprehension list: for every i in the range from 1 to smaller than 101, save in the list i to the 2nd power if i is multiple of 3.

    # challenge : Create, using a comprehension list, a list of all multiple of 4, 6 and 9 until 5 digits.
    print([i for i in range(1, 100000) if i%4==0 and i%6==0 and i%9==0 ])

if __name__ == "__main__":
    main()