class Solution:
    def reverse(self, x: int) -> int:
        final = 0
        if x >= 0:
            final = int(str(x)[::-1])
        else:
            final = -int(str(x)[1:][::-1])

        if not (-2**31 <= final <= 2 ** 31 - 1):
            return 0
        else:
            return final