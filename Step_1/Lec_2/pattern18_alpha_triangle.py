def alpha_triangle(n):
    for i in range(1,n+1):
        for ch in range(ord('A')+n-i, ord('A')+n):
            print(chr(ch), end=' ')
            ch += 1
        print()




def main():
    number = int(input("Enter an Integer: "))
    alpha_triangle(number)



if __name__ == "__main__":
    main()
