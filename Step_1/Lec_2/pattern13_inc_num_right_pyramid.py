def inc_num_pyramid(n):
    num = 1
    for i in range(n):
        for j in range(i+1):
            print(num, end = " ")
            num += 1
        print()



def main():
    number = int(input("Enter an Integer: "))
    inc_num_pyramid(number)



if __name__ == "__main__":
    main()
