#rsait001 Ryota Saito 
# writing "cat" cmd in python 

#imports
import sys

#pop off hw1.py from the cmd line
sys.argv.pop(0)

#check for 0 args (1 is the base command) 
if len(sys.argv) > 0:

	#parse files (i returns files name)
 	for i in sys.argv:

		#open file, read it and print it
		file = open(i, 'r')
		print "---------------------------------------------------------------------------------------------------------------------------------------------"
		print i 
		print file.read()

else:
	print "Must supply file(s)" 
