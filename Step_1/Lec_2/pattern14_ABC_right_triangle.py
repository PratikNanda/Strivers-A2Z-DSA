def alpha_right_triangle(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(65+j), end = " ") # Ascii 65 is A 
        print()

def pattern14(N):
    # Outer loop for the number of rows
    for i in range(N):
        # Inner loop prints characters from 'A' to 'A' + i
        for ch in range(ord('A'), ord('A') + i + 1):
            print(chr(ch), end=' ')
        print()  # Line break after each row


def main():
    number = int(input("Enter an Integer: "))
    alpha_right_triangle(number)
    pattern14(number)



if __name__ == "__main__":
    main()
