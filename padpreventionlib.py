#Prevention Library for PadmeBot. Basically, this library helps in error prevention.
#Released under the GNU GPL v3.0. See COPYING for more information
class Preventor:
    def is_number(num):
        try:
            float(num)
            return True

        except Exception as e:
            return False
