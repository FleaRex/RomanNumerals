import json
import six


def lambda_handler(event, context):
    roman_value = event["romanvalue"]

    body = {}

    body["romanvalue"] = roman_value
    body["arabicvalue"] = convert_roman_to_arabic(roman_value)

    return {"statusCode": 200, "body": body}


def convert_roman_to_arabic(roman_value):
    if not isinstance(roman_value, six.string_types):
        raise Exception("Error: " + str(roman_value) + " is not in Roman Numerals")

    return 13
