#Math Library for PadmeBot
#Released under the BSD-new (3 clause) license. See COPYING for more information
import random
import math
import padpreventionlib

class Mathematics:
    def generate_32bit():
        number = random.getrandbits(32)
        return 'Your 32-bit number: ' + str(number)

    def generate_64bit():
        number = random.getrandbits(64)
        return 'Your 64-bit number: ' + str(number)


    def get_sin(num):
        preventor = padpreventionlib.Preventor
        is_number = preventor.is_number(num)

        if is_number is True:
            number = math.sin(math.radians(float(num)))
            return 'Sin value: ' + str(number)

        else:
            return 'That is not a number!'


    def get_cos(num):
        preventor = padpreventionlib.Preventor
        is_number = preventor.is_number(num)

        if is_number is True:
            number = math.cos(math.radians(float(num)))
            return 'Cos value: ' + str(number)

        else:
            return 'That is not a number!'

    def get_tan(num):
        preventor = padpreventionlib.Preventor
        is_number = preventor.is_number(num)

        if is_number is True:
            number = math.tan(math.radians(float(num)))
            return 'Tan value: ' + str(number)

        else:
            return 'That is not a number!'
