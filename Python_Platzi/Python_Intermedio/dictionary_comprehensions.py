def main():
    # Create a dict and populate using a for loop.
    # my_dict={}
    # for i in range(1, 101):
    #     dictionary[i]=i**3

    """
                Dictionary comprehensions
    { key:value   for value in iterable     if condition  }
    {  [part 1]          [part 2]               [part 3]  }
    
    part 1: represent every key and value to put in the new dictionary.
    part 2: Loop to extract the elements of any iterable.
    part 3: Condition to filter the elements of the loop.
    # """    
    # my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}

    # print(my_dict)

    # challenge: Create a dictionary comprehension which keys are the first


if __name__ == "__main__":
    main()