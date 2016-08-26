# -*- coding: utf-8 -*-

import math

a = float(input())
b = float(input())

print('%d°' % int(round(math.degrees(math.atan(a/b)))))

