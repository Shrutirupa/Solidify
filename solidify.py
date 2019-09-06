#Aim: A tool for writing solidity codes for smart contracts using Python
#Name: Shrutirupa Banerjiee
#Date: 6.9.2019

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Modules to be imported

import sys
import os.path
import getopt
from sys import argv, stdout

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Function: usage
#Purpose: To help the users to understand the usage of the tool

def usage(script):
	"To provide help to the users on the usage of the tool"
	print ("\n \n %s [-i]" %script)
	print ("\n this is how the user is supposed to")
	print (" enter data in the command line")
	print ("\n -i [--in]  : The file name for the solidity code")
	print ("\n \n ")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def firstStep(fileName):
	"To add an extention to the end of the file"
	print "I guess i am in firstStep function \n"
	pass

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Function: main
#Purpose: The main function 

def main(argv):
	"To take the name of the solidity file through command line"
	fileName = ""
	if len(argv) < 2:
		usage(this_script)
		sys.exit(1)

	try:
		opts, args = getopt.getopt(argv[1:], "i:",["in="])

	except getopt.GetoptError:
		usage(this_script)
		sys.exit(2)

	pass

	for opt, arg in opts:
		
		if opt in ("-i", "--in"):
			fileName = arg

	if ( fileName == ""):
		print ("\n proper filename has to be given")	
		return(-3)

	pass

	firstStep(fileName)
	
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Purpose: To kickstart

if __name__=="__main__":
	main(sys.argv[0:])

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
