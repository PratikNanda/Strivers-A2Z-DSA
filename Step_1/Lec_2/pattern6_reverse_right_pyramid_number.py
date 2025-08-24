def reverse_triangle_num(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print(f"{j+1} ",end="")
        print()


def main():
    number = int(input("Enter an Integer: "))
    reverse_triangle_num(number)



if __name__ == "__main__":
    main()
