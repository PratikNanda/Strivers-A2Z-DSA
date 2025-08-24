# def rectangle(n):
#     for i in range(n):
#         for j in range(n):
#             print("* ",end = "")
#         print()


def rectangle(n):
    for i in range(n):
        print("* "*n)


def main():
    number = int(input("Enter an Integer: "))
    rectangle(number)



if __name__ == "__main__":
    main()
