#!/usr/bin/env python3
import sys

#Author: Yazan Elmadhoun
#Author ID: yelmadhoun

if len (sys.argv) == 1:
	timer = 3
else:
	timer =int(sys.argv[1])
while timer > 0:
	print(timer)
	timer -= 1
print('blast off!')
