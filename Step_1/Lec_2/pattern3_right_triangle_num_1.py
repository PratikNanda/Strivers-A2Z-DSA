def right_angled_pyramid_1(n):
    for i in range(n):
        for j in range(i+1):
            print(f"{j+1} ",end = "")
        print()

def main():
    number = int(input("Enter an Integer: "))
    right_angled_pyramid_1(number)



if __name__ == "__main__":
    main()
