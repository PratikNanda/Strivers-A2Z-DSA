def alpha_pyramid(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end = " ")
        ch = ord('A')
        breakpoint = (2*i + 1) // 2
        for l in range(2*(i+1)-1):
            print(chr(ch), end=' ')
            if l < breakpoint :
                ch += 1
            else:
                ch -= 1
        for k in range(n-i-1):
            print(" ",end = " ")
        print()



def main():
    number = int(input("Enter an Integer: "))
    alpha_pyramid(number)



if __name__ == "__main__":
    main()
