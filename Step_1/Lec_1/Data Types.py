
def datatype():
    io = input()
    print(type(io))
    print(type(int(io)))
    print(type(float(io)))
    print(type(1j))
    print(type(["apple", "banana", "cherry"]))
    print(type(("apple", "banana", "cherry")))
    print(type(range(6)))
    print(type({"name" : "John", "age" : 36}))
    print(type({"apple", "banana", "cherry"}))
    print(type(frozenset({"apple", "banana", "cherry"})))
    print(type(True))
    print(type(str(True)))
    print(type(b"Hello"))
    print(type(bytearray(5)))
    print(type(memoryview(bytes(5))))
    print(type(None))
    print(type(str(None)))
    print(type(io))




def main():
    datatype()



if __name__ == "__main__":
    main()