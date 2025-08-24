def reverse_star_pyramid(n):
    for i in range(n, 0, -1):
        for _ in range(n-i):
            print(" ", end = "")
        for _ in range(2*i - 1):
            print("*", end = "")
        for _ in range(n-i):
            print(" ",end = "")
        print()
        

def main():
    number = int(input("Enter an Integer: "))
    reverse_star_pyramid(number)



if __name__ == "__main__":
    main()
