#!/usr/bin/env python
import re

def convert(oldcode):
    'Convert the old code to the new code.'
    if '+' in oldcode:
        beforeplus, afterplus = oldcode.split('+')
    else:
        beforeplus = oldcode

    z, x, q = [int(re.sub(r'[^0-9]', '',thing)) for thing in  oldcode.split('.')]

    rightsideup = z == 5

    if q == 0:
        angle = x
    elif q ==1:
        angle = x
    elif q == 2:
        angle = 180 - x
    elif q == 3:
        angle = 270

    return (angle, rightsideup)
