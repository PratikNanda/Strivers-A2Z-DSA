def rev_arr(i,n,arr):
    if i >= n//2:
        return
    arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
    rev_arr(i+1,n,arr)


def main():
    array = []
    n = int(input("length of array: "))
    for _ in range(n):
        array.append(int(input()))
    print(array)
    rev_arr(0,n,array)
    print(array)



if __name__ == "__main__":
    main()