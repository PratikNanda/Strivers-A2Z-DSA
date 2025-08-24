def alpha_ramp(n):
    for i in range(n):
        ch = chr(ord('A') + i)
        print((ch + ' ') * (i + 1))

# def alpha_ramp(n):
#     ch = ord('A')
#     for i in range(n):
#         for j in range(i + 1):
#             print(chr(ch), end=' ')
#         print()
#         ch = ch + 1


def main():
    number = int(input("Enter an Integer: "))
    alpha_ramp(number)



if __name__ == "__main__":
    main()
