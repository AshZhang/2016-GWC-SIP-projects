from hashlib import *
import string

rainbow = {}
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

for i in list(string.ascii_letters):
	for j in list(string.ascii_letters):
		for k in list(string.ascii_letters):
			string = i+j+k
			print(string)