def pattern20(n):
    for i in range(2*n):
        if i < n:
            for j in range(i+1):
                print("*",end="")
            print(" "*((2*n) - (2*(i+1))), end = "")
            for j in range(i+1):
                print("*",end="")
            print()
        else:
            for j in range(((2*n)-i-1),0,-1):
                print("*",end="")
            print(" "*(2*(i+1-n)),end = "")
            for j in range(((2*n)-i-1),0,-1):
                print("*",end="")
            print()


def main():
    num = int(input("Enter number: "))
    pattern20(num)



if __name__ == "__main__":
    main()