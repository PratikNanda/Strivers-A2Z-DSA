def pattern22(n):
    # Outer loop for rows
    for i in range(2 * n - 1):
        # Inner loop for columns
        for j in range(2 * n - 1):
            # Initializing top, bottom, left, right indices
            top = i
            left = (2 * n - 2) - i
            bottom = j
            right = (2 * n - 2) - j
            
            # Minimum of 4 directions, subtracted from n
            value = n - min(top, bottom, left, right)
            print(value, end=" ")
        print()  # New line after each row


            
        

def main():
    num = int(input("Enter number: "))
    pattern22(num)



if __name__ == "__main__":
    main()