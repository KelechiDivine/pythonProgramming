from LoggerError import error
from LoggerError import debug
from LoggerError import info
from LoggerError import critical
from LoggerError import warn

try:
    a = 1/0

except:
    error("something went wrong")