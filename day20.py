#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
ns=0
for i in range(n):
    for j in range(n-1):
        if(a[j] > a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
            ns=ns+1
if(ns==0):
    print("Array is sorted in 0 swaps.")
else:
    print("Array is sorted in {} swaps.".format(ns))   
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[n-1]))                
