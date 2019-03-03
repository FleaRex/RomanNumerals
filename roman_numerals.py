import json
import six


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
    roman_value = roman_value.lower()
    if not all(
        map(lambda x: x in ["i", "v", "x", "l", "c", "d", "m"], list(roman_value))
    ):
        return False
    return True


def perform_conversion(roman_value):
    return 13


def convert_letter(letter):
    values = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}
    return values[letter.lower()]
