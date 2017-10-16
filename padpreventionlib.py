#Prevention Library for PadmeBot. Basically, this library helps in error prevention.
#Released under the BSD-new (3 clause) license. See COPYING for more information
class Preventor:
    def is_number(num):
        try:
            float(num)
            return True

        except Exception as e:
            return False

    def is_divide_by_zero(num):
        try:
            number = 1 / num
            return False

        except ZeroDivisionError:
            return True

    def is_negative(num):
        number = 1 / num

        if number <= -1:
            return True

        else:
            return False
