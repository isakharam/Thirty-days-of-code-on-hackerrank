import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    lst = bin(n)
    lst=lst[2:]
    print(max(map(len, lst.split("0"))))    
