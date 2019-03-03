from roman_numerals import convert_roman_to_arabic


class TestRomanToArabic(object):
    def test_basic(self):
        assert convert_roman_to_arabic("test") == 13
