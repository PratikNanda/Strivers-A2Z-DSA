# count = 0

# def recurse_name(n,name):
#     global count
#     if count == n:
#         return
#     print(f"Printing my name {n} times.\nThis is occurence number:{count+1}\n{name}\n")
#     count += 1
#     recurse_name(n,name)


#  -------------Without Global Variable----------------

def recurse_name(i,num,name):
    if i > num:
        return
    print(f"{name}")
    recurse_name(i+1,num,name)

def main():
    name = input("Enter your name: ")
    number = int(input("Enter your number: "))
    recurse_name(1,number,name)


if __name__ == "__main__":
    main()
    