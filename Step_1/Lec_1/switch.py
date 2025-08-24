def whichWeekDay(day):
        match day:
            case 1:
                print("Monday")
            case 2:
                print("Tuesday")
            case 3:
                print("Wednesday")
            case 4:
                print("Thursday")
            case 5:
                print("Friday")
            case 6:
                print("Saturday")   
            case 7:
                print("Sunday")
            case _:
                print("Invalid")   

def main():
    day = int(input())
    whichWeekDay(day)

if __name__ == "__main__":
    main()