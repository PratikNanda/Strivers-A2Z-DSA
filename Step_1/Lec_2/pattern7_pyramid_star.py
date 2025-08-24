# def star_pyramid(n):
#     for i in range(n):
#         for j in range(n-i-1):
#             print(" ", end = "")
#         print("*"+"*"*(2*i))


def star_pyramid(n):
    for i in range(n):
        for _ in range(n-i-1):
            print(" ",end = "")
        for _ in range(2*i + 1):
            print("*", end = "")
        for _ in range(n-i-1):
            print(" ",end = "")
        print()




def main():
    number = int(input("Enter an Integer: "))
    star_pyramid(number)



if __name__ == "__main__":
    main()
