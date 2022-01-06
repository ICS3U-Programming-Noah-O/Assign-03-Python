#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: Dec. 14, 2021
# This program allows a user to input the weight
# and volume of a package to see if a company will accept it.

import colorama
import random
import time
from colorama import Fore, Back, Style


def main():
    # Function that calculates volume in cm
    def units_cm():

        if package_volume > 10000 and package_weight_float > weight_num:
            print(Fore.RED + "Sorry, {}".format(package_weight_float)
                  + "{} is too heavy".format(unit_weight)
                  + " and {}cm^3 is too large.".format(package_volume))
            print(" ")

        elif package_volume > 10000:
            print(Fore.RED + "Sorry, {}".format(package_weight_float) +
                  "{} is ok,".format(unit_weight) +
                  " but {}cm^3 is too large.".format(package_volume))
            print(" ")

        elif package_weight_float > weight_num:
            print(Fore.RED + "Sorry, {}".format(package_weight_float) +
                  "{} is too heavy,".format(unit_weight) +
                  " but {}cm^3 is ok.".format(package_volume))
            print(" ")

        else:
            print(" ")
            print(Fore.YELLOW + "That package is acceptable!")
            print("Thank you for choosing Bob’s Box delivery service.")
            print(" ")

    # Function that calculates volume in mm
    def units_mm():

        if package_volume > 100000 and package_weight_float > weight_num:
            print("Sorry, {}".format(package_weight_float) +
                  "{} is too heavy".format(unit_weight) +
                  " and {}mm^3 is too large.".format(package_volume))
            print(" ")
        elif package_volume > 100000:
            print("Sorry, {}".format(package_weight_float) +
                  "{} is ok,".format(unit_weight) +
                  " but {}mm^3 is too large.".format(package_volume))
            print(" ")
        elif package_weight_float > weight_num:
            print("Sorry, {}".format(package_weight_float) +
                  "{} is too heavy,".format(unit_weight) +
                  " but {}mm^3 is ok.".format(package_volume))
            print(" ")
        else:
            print(package_volume)
            print("That package is acceptable!")
            print("Thank you for choosing Bob’s Box delivery service.")
            print(" ")

    # Function that calculates volume in ft
    def units_ft():

        if package_volume > 328.084 and package_weight_float > weight_num:
            print(Fore.RED + "Sorry, {}".format(package_weight_float) +
                  "{} is too heavy".format(unit_weight) +
                  " and {}ft^3 is too large.".format(package_volume))
            print(" ")
        elif package_volume > 328.084:
            print(Fore.RED + "Sorry, {}".format(package_weight_float) +
                  "{} is ok,".format(unit_weight) +
                  " but {}ft^3 is too large.".format(package_volume))
            print(" ")
        elif package_weight_float > weight_num:
            print(Fore.RED + "Sorry, {}".format(package_weight_float) +
                  "{} is too heavy,".format(unit_weight) +
                  " but {}ft^3 is ok.".format(package_volume))
            print(" ")
        else:
            print(package_volume)
            print("That package is acceptable!")
            print(Fore.YELLOW +
                  "Thank you for choosing Bob’s Box delivery service.")
            print(" ")

    # Prints intro message
    print(Fore.WHITE + "Thank you for using Bob’s Box delivery service.")
    print(Fore.BLUE + "This program can tell you if we are able to " +
          "accept your package for delivery.")
    print(Fore.RED + "We cannot take packages that are over 27 kg " +
          "in weight or 10000 cubic cm in volume.")
    print(" ")
    time.sleep(1)
    unit_volume = (input(Fore.WHITE + "Enter the unit that you would to " +
                   "use to measure the volume cm/mm/ft: "))
    print(" ")

    # Determines if the user input for volume unit is valid
    if unit_volume == "cm":
        print(" ")
    elif unit_volume == "mm":
        print(" ")
    elif unit_volume == "ft":
        print(" ")
    else:
        print("Invalid volume unit.")
        return

    unit_weight = (input("Enter the unit that you would to use" +
                   " to measure the weight kg/g/mg: "))
    print(" ")

    # Determines if the user input for weight unit is valid
    if unit_weight == "kg":
        weight_num = 27
    elif unit_weight == "g":
        weight_num = 27000
    elif unit_weight == "mg":
        weight_num = 27000000
    else:
        print("Invalid weight unit")
        return

    time.sleep(1)
    package_weight = (input("Enter the weight of your package " +
                      "in {}: ".format(unit_weight)))
    print(" ")

    try:
        # Make sure user input is an integer
        package_weight_float = float(package_weight)

        if package_weight_float <= 0:
            print("'{}' is not a valid number".format(package_weight))
            print(" ")
            main()
            return

    except Exception:
        # Prevent crash by displaying error messsage
        print("'{}' is not a number".format(package_weight))
        print(" ")
        main()
        return

    time.sleep(1)
    package_height = (input("Enter the height of your package " +
                      "in {}: ".format(unit_volume)))
    print(" ")

    try:
        # Make sure user input is an integer
        package_height_float = float(package_height)

        if package_height_float <= 0:
            print("'{}' is not a valid number".format(package_height))
            print(" ")
            main()
            return

    except Exception:
        # Prevent crash by displaying error messsage
        print("'{}' is not a number".format(package_height))
        print(" ")
        main()
        return

    time.sleep(1)
    package_length = (input("Enter the length of your package " +
                      "in {}: ".format(unit_volume)))
    print(" ")

    try:
        # Mqke sure user input is an integer
        package_length_float = float(package_length)

        if package_length_float <= 0:
            print("'{}' is not a valid number".format(package_length))
            print(" ")
            main()
            return

    except Exception:
        # Prevent crash by displaying error messsage
        print("'{}' is not a number".format(package_length))
        print(" ")
        main()
        return

    time.sleep(1)
    package_width = (input("Enter the width of your package " +
                     "in {}: ".format(unit_volume)))
    print(" ")

    try:
        # Make sure user input is an integer
        package_width_float = float(package_width)

        if package_width_float <= 0:
            print("'{}' is not a valid number".format(package_width))
            print(" ")
            main()
            return

    except Exception:
        # Prevent crash by displaying error messsage
        print("'{}' is not a number".format(package_width))
        print(" ")
        main()
        return

    # Calculate final package volume
    package_volume = (package_length_float * package_width_float *
                      package_height_float)

    # Call specific function based on user inputted units
    if unit_volume == "cm":
        units_cm()
    elif unit_volume == "mm":
        units_mm()
    elif unit_volume == "ft":
        units_ft()


def end():
    print("end")


if __name__ == "__main__":
    main()
