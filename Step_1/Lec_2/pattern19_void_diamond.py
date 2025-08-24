def pattern19(n):
    for i in range(2*n):
        if i < n:
            for j in range(n-i):
                print("*",end="")
            print(" " *2*i,end = "")
            for j in range(n-i):
                print("*",end="")
            print()
        else:
            for j in range(i+1-n):
                print("*", end = "")
            print(" "*2*((2*n)-i-1), end = "")
            for j in range(i+1-n):
                print("*", end = "")
            print()
            

            



def main():
    num = int(input("Enter number: "))
    pattern19(num)



if __name__ == "__main__":
    main()