count = 0

def recursion(n):
    global count
    if count == n:
        return
    print(f"printing {n} times. This is {count+1} time")
    count += 1
    recursion(n)

def main():
    number = int(input("Enter your number: "))
    recursion(number)


if __name__ == "__main__":
    main()
    