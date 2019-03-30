# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 22:08:16 2019

@author: ganapathy

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

"""
### My option #####
inlist=[1, 2, 3, 4, 5]
templist=inlist.copy()
outlist=[]
for i in range(len(inlist)):
    templist.pop(i)
    result=1
    for j in templist:
        result=j*result
    templist=inlist.copy()
    outlist.append(result)
print(outlist)

##### Joe's option (this is a better solution)#############

inlist=[1, 2, 3, 4, 5]
outlist=[]
for i in range(len(inlist)):
    result=1
    for j in range(len(inlist)):
        if j!=i:
            result*=inlist[j]
    outlist.append(result)
print(outlist)

##### note: Typo i instead of j, result*=inlist[i] resulted in multiplying the same number len(inlist)-1 times#############
