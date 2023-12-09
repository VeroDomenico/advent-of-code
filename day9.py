import re
from functools import cmp_to_key
from functools import reduce
from enum import IntEnum
from collections import Counter
from functools import cmp_to_key
import math


def resSerries(series):
    if all(series[i] == series[0] for i in range(1, len(series))):
        return series[0]
    newSeries = []
    for i in range(len(series)-1):
        newSeries.append(series[i+1] - series[i])
    return series[0] - resSerries(newSeries)



# import file
file = open(, "r")
data = file.readlines()
sum = 0
for line in data:
    line = line.strip()
    series = [int(x) for x in line.strip().split(" ")]
    sum += resSerries(series)
    
print(sum)
