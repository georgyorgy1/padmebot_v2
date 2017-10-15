#Logging library for PadmeBot
#Released under the GNU GPL v3.0. See COPYING for more information
import datetime

class Clock:
    def get_curr_datetime():
        now = datetime.datetime.now()
        time_format = '%I:%M:%S %p'
        date = str(now.month) + "-" + str(now.day) + "-" + str(now.year)
        time = str(datetime.datetime.now().strftime(time_format))
        return date + ", " + time

class Printer:
    def open_file():
        return open('botlog.txt', 'a')

    def write_log(event):
        f = Printer.open_file()
        f.write(Clock.get_curr_datetime() + ": " + str(event))
        f.write('\n')
        f.close()

    def say(string):
        print(Clock.get_curr_datetime() + ": " + str(string))
        Printer.write_log(string)
