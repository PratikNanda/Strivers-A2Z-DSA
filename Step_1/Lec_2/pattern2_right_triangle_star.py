def right_triangle(n):
    for i in range(n):
        for j in range(i+1):
            print("* ",end = "")
        print()

def R_triangle(n):
    for i in range(n):
        print("* "*(i+1))


def main():
    number = int(input("Enter an Integer: "))
    right_triangle(number)
    R_triangle(number)



if __name__ == "__main__":
    main()
