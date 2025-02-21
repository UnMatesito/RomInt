roman_dict = [
    ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
    ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
    ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)
]

def roman_to_number(roman_number):
    if (roman_number == "IIII"):
        print("Inexistent number")
        exit()

    number = 0

    while (roman_number != ""):
        for number, symbol in roman_dict:
            print("")


    


def number_to_roman(number):
    if (number > 3999):
        print("The number is 4000 or grater")
        exit()

    roman_number = ""

    while number != 0:
        for symbol, value in roman_dict:
            if value <= number:
                roman_number += symbol
                number -= value
                break

    return roman_number


#print("Roman/Number converter")

#print("Select an option: \n"
#      "1. Roman to Number \n"
#     "2. Number to Roman")

#option = input("Enter option: ")

#if (option == 1):
#    roman = input("Enter Roman number: ")
#    print("Number: ", roman_to_number(roman))
#else:
number = int(input("Enter number: "))
print("Roman: ", number_to_roman(number))
