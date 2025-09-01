def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
        


def main():
    number = int(input("Enter your number: "))
    if is_prime(number):
        print ("The given number is prime number")
    else: 
        print ("The given number is not a prime number")

if __name__ == "__main__":
    main()