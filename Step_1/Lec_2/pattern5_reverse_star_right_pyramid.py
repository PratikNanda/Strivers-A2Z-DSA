# def reverse_triangle(n):
#     v = n
#     for i in range(n):
#         for j in range(v):
#             print("* ",end = "")
#         v = v - 1
#         print()

def reverse_triangle(n):
    for i in range(n, 0, -1):
        print("* "*i)


def main():
    number = int(input("Enter an Integer: "))
    reverse_triangle(number)



if __name__ == "__main__":
    main()
