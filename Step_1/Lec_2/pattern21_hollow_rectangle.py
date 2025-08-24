def pattern21(n):
    for i in range(n):
        if i == 0 or i == (n-1):
            for j in range(n):
                print("*",end="")
        else:
            print("*",end ="")
            for j in range(n-2):
                print(" ",end = "")
            print("*",end ="")
        print()




def main():
    num = int(input("Enter number: "))
    pattern21(num)



if __name__ == "__main__":
    main()