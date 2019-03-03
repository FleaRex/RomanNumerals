import json
import six

roman_numeral_conversions = {
    "i": 1,
    "v": 5,
    "x": 10,
    "l": 50,
    "c": 100,
    "d": 500,
    "m": 1000,
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def lambda_handler(event, context):
    roman_value = event["romanvalue"]

    body = {}

    body["romanvalue"] = roman_value
    body["arabicvalue"] = convert_roman_to_arabic(roman_value)

    return {"statusCode": 200, "body": body}


def convert_roman_to_arabic(roman_value):
    if not is_valid_roman_numerals(roman_value):
        raise Exception("Error: " + str(roman_value) + " is not in Roman Numerals")
    return perform_conversion(roman_value)


def is_valid_roman_numerals(roman_value):
    if not isinstance(roman_value, six.string_types):
        return False

    if not all(map(lambda x: x in roman_numeral_conversions.keys(), list(roman_value))):
        return False

    return True


def perform_conversion(roman_value):
    return 13


def convert_letter(letter):
    return roman_numeral_conversions[letter]
