#!/usr/bin/env python3

# Created by: Brian Musembi
# Created on: 06 May 2021
# This program tells the month of the year


def main():
    # this function tells the month of the year

    # input
    month = int(input("Enter the number of a month (ex 3 for March): "))

    # process & output
    if (month == 1):
        print("January.")

    elif (month == 2):
        print("February.")

    elif (month == 3):
        print("March.")

    elif (month == 4):
        print("April.")

    elif (month == 5):
        print("May.")

    elif (month == 6):
        print("June.")

    elif (month == 7):
        print("July.")

    elif (month == 8):
        print("August.")

    elif (month == 9):
        print("September.")

    elif (month == 10):
        print("October.")

    elif (month == 11):
        print("November.")

    elif (month == 12):
        print("December.")

    else:
        print("")
        print("Please input a number from 1-12!")
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
