def get_divisors(n):
    lst = []
    for i in range(1,n+1):
        if n % i == 0:
            lst.append(i)
    return lst


def main():
    number = int(input("Enter your number: "))
    factors = get_divisors(number)
    print(factors)

if __name__ == "__main__":
    main()