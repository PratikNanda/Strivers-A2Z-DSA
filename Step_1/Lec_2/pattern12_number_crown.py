def number_crown(n):
    for i in range(1,n+1,1):
        for j in range(i):
            print(j+1,end = " ")
        for k in range(2*(n-i)):
            print(" ", end = " ")
        for j in range(i,0,-1):
            print(j,end = " ")
        print()
        


def main():
    number = int(input("Enter an Integer: "))
    number_crown(number)



if __name__ == "__main__":
    main()
