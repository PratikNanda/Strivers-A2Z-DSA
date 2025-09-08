def sum_of_N(n):
    if n == 0 :
        return 0;
    return n + sum_of_N(n-1)

def main():
    number = int(input("Enter your number: "))
    print(sum_of_N(number))


if __name__ == "__main__":
    main()


#----------------Parameterised way----------------------

# def sumN(i,sum):
#     if i < 1:
#         print(sum)
#         return
#     sumN(i-1,sum+i)


# def main():
#     number = int(input("Enter your number: "))
#     sumN(number,0)

# if __name__ == "__main__":
#     main()