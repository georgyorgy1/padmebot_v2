#Math Library for PadmeBot
#Released under the BSD-new (3 clause) license. See COPYING for more information
import math
import padpreventionlib

class Physics:
    def get_weight(mass):
        preventor = padpreventionlib.Preventor
        is_number = preventor.is_number(str(mass))

        if is_number is True:
            return 'Weight: ' + str(float(mass) * 9.8) + ' N'

        else:
            return 'That is not a number!'

    def get_speed(distance, time):
        preventor = padpreventionlib.Preventor
        is_number1 = preventor.is_number(str(distance))
        is_number2 = preventor.is_number(str(time))

        if is_number1 is True and is_number2 is True:
            return 'Speed in km/h: ' + str(float(distance) / float(time))

        else:
            return 'That is not a number!'

    def get_kinetic_energy(mass, velocity):
        preventor = padpreventionlib.Preventor
        is_number1 = preventor.is_number(str(mass))
        is_number2 = preventor.is_number(str(velocity))

        if is_number1 is True and is_number2 is True:
            return 'Kinetic Energy: ' + str(0.5 * float(mass) * math.pow(float(velocity), 2))

        else:
            return 'That is not a number!'
