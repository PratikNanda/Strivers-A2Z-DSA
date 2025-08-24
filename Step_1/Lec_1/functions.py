def tableof(n):
    table_in_list = []
    for i in range(10):
        print(n,"x",(i+1),"=",(i + 1)*n)
        table_in_list.append((i+1)*n)
    
    return table_in_list


def multiply_last_list(lst):
    lst[-1] = lst[-1]*10




def main():
    some = [1,2,3]
    print(some)
    number = int(input("Enter the Integer: "))
    print(tableof(number)) # pass by value
    multiply_last_list(some) # pass by reference
    print(some)


if __name__ == "__main__":
    main()

