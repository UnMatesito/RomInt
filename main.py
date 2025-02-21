roman_dict = [
    ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
    ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
    ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)
]

def roman_to_number(roman_number):
    if ("MMMM" in roman_number or "IIII" in roman_number or "VV" in roman_number):
        print("Inexistent number")
        exit()

    exp_number = 0

    while (roman_number != ""):
        for symbol, number in roman_dict:
            if (roman_number.startswith(symbol)):
                exp_number += number
                roman_number = roman_number[len(symbol):]
                break

    return exp_number


    


def number_to_roman(number):
    if (number > 3999):
        print("The number is 4000 or greater")
        exit()

    roman_number = ""

    while number != 0:
        for symbol, value in roman_dict:
            if value <= number:
                roman_number += symbol
                number -= value
                break

    return roman_number


print("Roman/Number converter")
print("Select an option: \n"
    "1. Roman to Number \n"
    "2. Number to Roman \n" 
    "3. exit")

while (True == True):

    option = input("Enter option: ")

    if (int(option) == 1):
        roman = input("Enter Roman number: ")
        print("Number: ", roman_to_number(roman))
    elif (int(option) == 2):
        number = int(input("Enter number: "))
        print("Roman: ", number_to_roman(number))
    else:
        break
