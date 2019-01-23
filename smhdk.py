import sys

#  Github : https://github.com/greyxploiter
#  Defri Indra M
#  Created on 22 Jan 2019

if __name__ == '__main__':
	if sys.version_info[0] < 3:
		sys.stdout.write("Must be using Python 3.x\n")
		exit()
	else:
		from assets import smhdk_class
		smhdk_class.main()
