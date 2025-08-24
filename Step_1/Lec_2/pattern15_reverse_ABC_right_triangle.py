def reverse_alpha_right_triangle(n):
    # Outer loop for the number of rows
    for i in range(n, 0, -1):
        # Inner loop prints characters from 'A' to 'A' + i
        for ch in range(ord('A'), ord('A') + i):
            print(chr(ch), end=' ')
        print()  # Line break after each row


def main():
    number = int(input("Enter an Integer: "))
    reverse_alpha_right_triangle(number)



if __name__ == "__main__":
    main()
