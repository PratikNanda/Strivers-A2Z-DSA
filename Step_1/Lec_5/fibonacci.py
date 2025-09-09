def Nfibo(n):
    if n <= 1:
        return n
    last = Nfibo(n-1)
    sLast = Nfibo(n-2)
    return last + sLast


def main():
    number = int(input("Enter your number: "))
    print(Nfibo(number))
    


if __name__ == "__main__":
    main()
    