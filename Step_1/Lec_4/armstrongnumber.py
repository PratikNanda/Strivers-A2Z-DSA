def is_armstrong(n):
    sum = 0
    dup = n
    digits = len(str(n))
    while n > 0:
        last_digit = n % 10
        sum += last_digit**digits
        n = n // 10
    return sum == dup


def main():
    number = int(input("Enter your number: "))
    if is_armstrong(number):
        print ("The given number is armstrong number")
    else: 
        print ("The given number is not an armstrong number")

if __name__ == "__main__":
    main()