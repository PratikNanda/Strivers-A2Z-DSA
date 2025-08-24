from pattern2_right_triangle_star import R_triangle
from pattern5_reverse_star_right_pyramid import reverse_triangle


def side_pyramid(n):
    for i in range(1,2*n,1):
        stars = i
        if i > n:
            stars = 2*n - i
        for j in range(stars):
            print("* ", end = "")
        print()

def main():
    number = int(input("Enter an Integer: "))

    side_pyramid(number)


    # R_triangle(number-1)
    # print("* "*number)
    # reverse_triangle(number-1)

if __name__ == "__main__":
    main()


