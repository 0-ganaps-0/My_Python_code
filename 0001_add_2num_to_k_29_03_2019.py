# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 23:35:06 2019

@author: ganapathy

This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

"""

def add_2_num_to_k(k,inlist):
    
    value='False'
    itr1=0
    while itr1 < len(inlist)-1:
        itr2=itr1+1
        while itr2 < len(inlist):
            print(itr1,itr2)
            if (inlist[itr1]+inlist[itr2]) == k:
                value='True'
                itr1=len(inlist)-1
                itr2=len(inlist)
            else:
                itr2+=1
        itr1+=1
    
    return value

k_=int(input())
inlist_=list(map(int,input().split()))
add_2_num_to_k(k_,inlist_)
