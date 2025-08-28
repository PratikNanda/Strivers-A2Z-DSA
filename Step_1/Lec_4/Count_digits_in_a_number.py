def count_digits(n):
    return len(str(n))

# def count_digits(n):
#     count = 0
#     convert = str(n)
#     for _ in convert:
#         count +=1
#     return count

# def count_digits(n):
#     count = 0
#     while n>0:
#         count += 1
#         n = n//10
#     return count


# import math
# def count_digits(n):
#     count = int(math.log10(n)+1)
#     return count

def main():
    number = int(input("Enter the Number: "))
    digits = count_digits(number)
    print(digits)


if __name__ == "__main__":
    main()