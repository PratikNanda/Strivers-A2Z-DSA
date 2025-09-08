def fact_N(n):
    if n == 0 :
        return 1;
    return n * fact_N(n-1)

def main():
    number = int(input("Enter your number: "))
    print(fact_N(number))


if __name__ == "__main__":
    main()