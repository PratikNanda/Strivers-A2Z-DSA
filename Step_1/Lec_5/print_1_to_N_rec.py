# count = 0

# def recursion(n):
#     global count
#     if count == n:
#         return
#     print(f"{count+1}")
#     count += 1
#     recursion(n)

#  -------------Without Global Variable----------------

def rec_1_to_N(i,num):
    if i > num:
        return
    print(i)
    rec_1_to_N(i+1,num)

#----------Backtracking----------------

# def rec_1_to_N(i,num):
#     if i < 1:
#         return
#     rec_1_to_N(i-1,num) #give input as (N,N)
#     print(i)

def main():
    number = int(input("Enter your number: "))
    rec_1_to_N(1,number)


if __name__ == "__main__":
    main()
    