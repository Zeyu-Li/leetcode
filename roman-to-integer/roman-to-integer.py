class Solution:
    def romanToInt(self, s: str) -> int:
        # string to int array
        values = []
        key = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        for char in s:
            values.append(key[char])

        final_value = 0
        previous = values[0]
        for value in values:
            final_value+=value
            if value > previous:
                final_value-=2*previous
            previous = value

        return final_value
            
            