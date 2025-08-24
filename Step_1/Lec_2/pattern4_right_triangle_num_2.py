def right_angled_pyramid_2(n):
    for i in range(n):
        for j in range(i+1):
            print(f"{i+1} ",end = "")
        print()



def main():
    number = int(input("Enter an Integer: "))
    right_angled_pyramid_2(number)


if __name__ == "__main__":
    main()
