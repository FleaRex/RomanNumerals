import json

def lambda_handler(event, context):
    roman_value = event["romanvalue"]

    body = {}

    body["romanvalue"] = roman_value
    body["arabicvalue"] = convert_roman_to_arabic(roman_value)

    # raise Exception('Error: ' + roman_value + ' is not in Roman Numerals')

    return {
        'statusCode': 200,
        'body': body
    }


def convert_roman_to_arabic(roman_value):
    return 13
