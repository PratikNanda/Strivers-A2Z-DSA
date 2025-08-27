def reverse(x):
    reverse = 0
    sign = -1 if x < 0 else 1
    x = abs(x)
    while x:
        digit = x % 10
        reverse = reverse * 10 + digit
        x //= 10
    result = sign * reverse
    if result > 2 ** 31 - 1 or result < -(2 ** 31):
        return 0
    return result    



def main():
    number = int(input("Enter the Number: "))
    print(reverse(number))


if __name__ == "__main__":
    main()