import pytest
from roman_numerals import *


class TestRomanToArabic(object):
    def test_basic(self):
        assert convert_roman_to_arabic("xiii") == 13

    def test_case_insensitive(self):
        assert convert_roman_to_arabic("XIII") == 13

    def test_non_string_throws(self):
        with pytest.raises(Exception):
            convert_roman_to_arabic(12)

    def test_non_string_throws_with_error_message(self):
        try:
            convert_roman_to_arabic(12)
        except Exception as e:
            assert "Error:" in str(e)

    def test_non_roman_throws(self):
        with pytest.raises(Exception):
            convert_roman_to_arabic("cxvq")

    def test_convert(self):
        values = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}
        for roman, arabic in values.items():
            assert convert_letter(roman) == arabic
            assert convert_letter(roman.upper()) == arabic
