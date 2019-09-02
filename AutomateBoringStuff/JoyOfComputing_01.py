#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 01:48:23 2019

@author: gfx911
@URL:https://onlinecourses.nptel.ac.in/noc19_cs41/progassignment?name=259

Given an array A of N numbers (integers), you have to write a program which prints the sum of the elements of array A with the corresponding elements of the reverse of array A.
If array A has elements [1,2,3], then reverse of the array A will be [3,2,1] and the resultant array should be [4,4,4].

Input Format:
	The first line of the input contains a number N representing the number of elements in array A.
	The second line of the input contains N numbers separated by a space. (after the last elements, there is no space)

Output Format:
	Print the resultant array elements separated by a space. (no space after the last element)


"""
import os
# Clear Console
os.system('clear')

numList = input("Enter an array/list separated by space : ").split(" ")
print (numList)
print (numList[::-1])
total = 0
sumList = list()

sumList = [int(x)+int(y) for x,y in zip(numList, numList[::-1])]

print(sumList)
print("\n")
