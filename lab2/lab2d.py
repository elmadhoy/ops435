#!/usr/bin/env python3
import sys

#if len(sys.argv) > 2:



if len(sys.argv) != 3:
	print('Usage: ./lab2d.py name age')

if len(sys.argv) == 3:	
	name = sys.argv[1]		
	age = sys.argv[2]
	print('Hi ' + name + ', you are ' + str(age) + ' years old.')

