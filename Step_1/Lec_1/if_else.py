def studentGrade(marks):

        if marks >= 90:
            return "Grade A"
        elif marks >= 70:
            return "Grade B"
        elif marks >= 50:
            return "Grade C"
        elif marks >= 35:
            return "Grade D"
        else:
            return "Fail"

def main():
    marks = int(input("marks = "))
    print(studentGrade(marks))

if __name__ == "__main__":
    main()