def is_palindrome(i,s,l):
    if i > l//2: return True
    if s[i] != s[l-i-1]: return False
    return is_palindrome(i+1,s,l)




def main():
    string = input("Enter your string: ")
    n = len(string)
    if is_palindrome(0,string.lower(),n):
        print(f"Entered string '{string}' is a Palindrome")
    else:
        print(f"Entered string '{string}' is not a palindrome")





if __name__ == "__main__":
    main()