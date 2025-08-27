def reverse(x):
    reverse = 0
    x = abs(x)
    while x:
        digit = x % 10
        reverse = reverse * 10 + digit
        x //= 10
    return reverse   

def isPalindrome(x):
        dup = x
        reverse = 0

        while x>0:
            digit = x % 10
            reverse = reverse*10 + digit
            x = x//10
        
        if dup == reverse:
            return True
        else:
            return False


def main():
    number = int(input("Enter the Number: "))
    
    rev = reverse(number)
    if rev == number:
        print("given number is palindrome")
    else:
        print("not palindrome")
    
    if isPalindrome(number):
        print(number, "is a palindrome.")
    else:
        print(number, "is not a palindrome.")

if __name__ == "__main__":
    main()