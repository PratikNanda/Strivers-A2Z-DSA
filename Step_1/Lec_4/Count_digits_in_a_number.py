def count_digits(n):
    count = 0
    convert = str(n)
    for _ in convert:
        count +=1
    return count

   


def main():
    number = int(input("Enter the Number: "))
    total = count_digits(number)
    print(total)


if __name__ == "__main__":
    main()