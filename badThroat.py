# Written by Chadley Lyell ©2017

import os,readline
exit = False

eighty = "Setting volume to 80%"
twenty = "Done speaking. Setting volume to 20%"
saying = "Now speaking..."
header = "Please type what you would like to say:"

def main():
	global phrase
	print(header)
	phrase = input("> ")
	speak()

def speak():
	global phrase
	print(eighty)
	os.system('osascript -e "set Volume 5"')
	print(saying)
	os.system('say ' + phrase)
	print(twenty)
	os.system('osascript -e "set Volume 0.7"')
	print("Done!\n")
	main()

while exit == False:
	main()