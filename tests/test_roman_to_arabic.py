import pytest
from roman_numerals import convert_roman_to_arabic


class TestRomanToArabic(object):
    def test_basic(self):
        assert convert_roman_to_arabic("xiii") == 13

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
