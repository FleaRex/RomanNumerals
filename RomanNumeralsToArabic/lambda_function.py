import json

def lambda_handler(event, context):
    roman_value = event["romanvalue"]

    body = {}

    body["romanvalue"] = roman_value
    body["arabicvalue"] = 14

    # raise Exception('Error: ' + roman_value + ' is not in Roman Numerals')

    return {
        'statusCode': 200,
        'body': body
    }
