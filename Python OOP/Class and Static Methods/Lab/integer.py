class Integer:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def get_roman_value(roman_num):
        roman_nums = {
            'I': 1,
            'II': 2,
            'III': 3,
            'IV': 4,
            'V': 5,
            'VI': 6,
            'VII': 7,
            'VIII': 8,
            'IX': 9,
            'X': 10,
            'XI': 11,
            'XII': 12,
            'XIII': 13,
            'XIV': 14,
            'XV': 15,
            'XVI': 16,
            'XVII': 17,
            'XVIII': 18,
            'XIX': 19,
            'XX': 18,
        }
        return roman_nums[roman_num]

    @classmethod
    def from_float(cls, float_value):
        if type(float_value) == int or type(float_value) == str:
            return "value is not a float"
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value):
        return cls(cls.get_roman_value(value))

    @classmethod
    def from_string(cls, value):
        if type(value) == str:
            return cls(int(value))
        return "wrong type"


# Test code:

first_num = Integer(10)
print(first_num.value)
second_num = Integer.from_roman("IV")
print(second_num.value)
print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
