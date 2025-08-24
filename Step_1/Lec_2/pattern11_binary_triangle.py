def binary_triangle(n):
    for i in range(n):
        for j in range(i+1):
            if (i+j)%2 == 0:
                print(1, end = " ")
            else:
                print(0, end = " ")
        print()



# def binary_triangle(n):
#     start = 1
#     for i in range(n):
#         if i%2 == 0:
#             start = 1
#         else:
#             start = 0
#         for j in range(i+1):
#             print(start, end =" ")
#             start = 1 - start

#         print()


# def binary_triangle(n):
#     for i in range(n):
#         for j in range(i+1):
#             if i%2 == 0:
#                 if j%2 == 0:
#                     print(1, end = " ")
#                 else:
#                     print(0, end = " ")
#             else:
#                 if j%2 == 0:
#                     print(0, end = " ")
#                 else:
#                     print(1, end = " ")
#         print()
            





def main():
    number = int(input("Enter an Integer: "))
    binary_triangle(number)



if __name__ == "__main__":
    main()
