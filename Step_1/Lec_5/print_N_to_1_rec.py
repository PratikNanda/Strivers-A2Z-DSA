# def rec_N_to_1(i,num):
#     if i < 1:
#         return
#     print(i)
#     rec_N_to_1(i-1,num)


#----------Backtracking----------------

def rec_N_to_1(i,num):
    if i > num:
        return
    rec_N_to_1(i+1,num)
    print(i)

def main():
    number = int(input("Enter your number: "))
    rec_N_to_1(1,number)


if __name__ == "__main__":
    main()
    