"""
given a time in AM/PM format, convert to military time
07:05:45PM
19:05:45
"""
from time import strptime
am_pm = '07:05:45PM'
a = strptime(am_pm, '%I:%M:%S%p')

def zero_converter(num):
    if num < 10:
        return '0{}'.format(num)
    else:
        return str(num)

print '{}:{}:{}'.format(zero_converter(a.tm_hour), zero_converter(a.tm_min), zero_converter(a.tm_sec))
