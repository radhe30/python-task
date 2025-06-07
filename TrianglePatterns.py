# Created by Radha Mohan
# Assignment: Print Triangle Patterns (Lower, Upper, Pyramid)
# Date: 6 June 2025

def lower_triangle(n):
    print("Lower Triangular Pattern:")
    for i in range(1, n + 1):
        print("* " * i)
    print()  



def upper_triangle(n):
    print("Upper Triangular Pattern:")
    for i in range(n, 0, -1):
        print("* " * i)
    print() 


def pyramid(n):
    print("Pyramid Pattern:")
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '* ' * i
        print(spaces + stars)
    print() 


if __name__ == "__main__":
    
    rows = int(input("Enter number of rows: "))

    
    lower_triangle(rows)
    upper_triangle(rows)
    pyramid(rows)