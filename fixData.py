import sys
import os.path
import time
import itertools

def Main():
	finalNames = open("finalNames.txt", "a")
	with open("Male.txt", "r") as ins:
	    array = []
	    for line in ins:
	        array.append(line)
	split = []
	for elem in array:
		split.append(elem.split())
	finalM = []
	for elem in  split:
		finalM.append(elem[0])
	# print(finalM[30])

	with open("female.txt", "r") as ins:
	    array = []
	    for line in ins:
	        array.append(line)
	split = []
	for elem in array:
		split.append(elem.split())
	finalF = []
	for elem in  split:
		finalF.append(elem[0])
	# print(finalF[20])

	outputList = list(set(itertools.chain(finalM, finalF)))
	print(len(outputList))


	for item in outputList:
		# print(item)
		finalNames.write(item + "\n")

Main()