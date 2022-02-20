# Author: Matthew Klatt
# Date created: 02-FEB-2022
import os
import sys
import glob
import random
import ctypes
import shutil
import platform
import requests
import colourCodes as cC

b_running = True
c_prefix = ';'
s_os_sys = platform.system()
s_os_rel = platform.release()
s_os_ver = platform.version()

os.system("CLS")
ctypes.windll.kernel32.SetConsoleTitleW("Simple clean up tool. | ScT - v1.1A") # Window title

print(f"{cC.b_CYAN}{cC.GREEN_b} Created by: Matthew. Klatt {cC.reset}")
print(f"{cC.b_YELLOW} Type ';help' if needed. \n {cC.reset}")
s_inputDisplayText = f"{cC.b_MAGENTA}> {cC.b_CYAN}"




# Define functions #################################################################
def moveFiles():
	print(f"{cC.b_GREEN} Moving files . . . {cC.reset}")
	for file in sourcefiles:
		if file.endswith('.' + s_userInput):
			shutil.move(os.path.join(dir, file), os.path.join(s_fileDestination, file))

def colourReset():
	print(f"{w_Foreground} {w_Background}"); os.system("CLS")

####################################################################################




while b_running:
	dir = os.getcwd() # current dir . . .
	sourcefiles = os.listdir()
	print(cC.b_WHITE + dir)

	s_userInput = str(input(s_inputDisplayText)) # get userinput . . .
	s_fileDestination = dir + "\\" + s_userInput
	print(cC.reset)

	# if the first char of the string begins with the chosen prefix,
	# then cut the first char from the string (prefix) and check the command list.
	if s_userInput.startswith(c_prefix, 0,1):
		#s_userInput = s_userInput.lower()[1:]
		s_userInput = s_userInput.lower()


		# commands . . .
		if ";cd" in s_userInput: # change dir . . .
			s_userInput = s_userInput[4:]

			if os.path.isdir(s_userInput): # check if path / directory exists . . .
				os.chdir(s_userInput)
			else:
				print(cC.b_RED + "Could not find that directory, please check spelling. \n" + cC.reset)

		elif ";webgrab" in s_userInput:
			s_userInput = s_userInput[9:]

			"""s_userInput = s_userInput.replace('https://www.', '')
			s_userInput = s_userInput.replace('http://www.', '')
			s_userInput = s_userInput.replace('.com', '')
			s_userInput = s_userInput.replace('.org', '')
			#s_userInput = s_userInput.replace('/', '_')"""

			saveas = s_userInput[s_userInput.index('/')+1:]
			#s_userInput = s_userInput[s_userInput.index('/')+1:]

			print(f"saveas {saveas}")
			print(f"s_userInput {s_userInput} \n\n")




			open(saveas, "wb").write(requests.get(s_userInput, allow_redirects=True).content)


		elif ";mkdir" in s_userInput and len(s_userInput) > 0: # Create folder . . .
			s_userInput = s_userInput[7:]
			s_userInput = s_userInput.replace('\'', '')
			s_userInput = s_userInput.replace('\"', '')
			#s_userInput = s_userInput.replace(' ', '_')

			if not os.path.isdir(s_userInput):
				print(f"{cC.b_GREEN} Creating folder . . . {cC.reset}")
				os.makedirs(s_userInput)
			else:
				print(f"{cC.b_RED} Folder already exists. {cC.reset}")

		elif ";help" in s_userInput: # Display help commands . . .
				print(f"{cC.b_YELLOW}")
				print(f";clr will clear the console window. \n")
				print(f";cd will let you change your working directory. \n")
				print(f";open will let you run/open a file/directory. \n")
				print(f";mkdir will let you create a new folder inside of the current directory you are in. \n")
				print(f";mfile will let you create new files in the current directory you are in. \n")
				print(f";os will display current os version information. \n")
				print(f";dir will list all files in the current directory. \n")
				print(f";die will kill the console. \n")
				print(f";help will show these messages again. \n\n")
				print(f"To move files with a certian extention, simply type what you wish to move. EG: txt\nwill move all .txt file to a folder named \'txt\'.\n")
				print(f"{cC.reset}")

		elif ";dir" in s_userInput: # Show directory . . .
			for entry in os.scandir("."):
				if entry.is_file():
					print(f"{cC.CYAN} {entry.name} {cC.reset}")
				#else:
					#print(cC.MAGENTA + '[' + entry.name + ']' + cC.reset)
			for entry in os.scandir():
				if entry.is_dir():
					print(f"{cC.MAGENTA} [{entry.name}] {cC.reset}")

			print("\n")

		elif ";os" in s_userInput: # Get os version and realese . . .
			print(f"{s_os_sys} {s_os_rel} {s_os_ver}")

		elif ";open" in s_userInput and len(s_userInput) > 0: # Start function . . .
			s_userInput = s_userInput[6:]
			s_userInput = s_userInput.replace(' ', '')
			s_userInput = s_userInput.replace('/', '')
			#s_userInput = s_userInput.replace('\\', '')
			s_userInput = s_userInput.replace('\'', '')
			s_userInput = s_userInput.replace('\"', '')
			if os.path.isfile(s_userInput) or os.path.isdir(s_userInput):
				os.startfile(s_userInput)
			else:
				print(f"{cC.b_RED} Can't seem to find what you're looking for . . . {cC.reset}")
				print(f"{cC.b_RED} Make sure you are in the right directory and to check your spelling. \n {cC.reset}")
			#os.system("start \"\" \"" + s_userInput + "\"")

		elif ";mfile" in s_userInput: # create file . . .
			s_userInput = s_userInput[7:]
			if os.path.isfile(s_userInput):
				print(f"{cC.b_RED} This file already exists . . . {cC.reset}")
			else:
				open(s_userInput, "x")

		elif ";nft" in s_userInput: # gen random 'nfts' . . .
			a_Colours = [cC.b_CYAN_b, cC.b_BLUE_b, cC.b_GREEN_b, cC.b_MAGENTA_b, cC.b_RED_b, cC.b_WHITE_b, cC.b_YELLOW_b]
			for x in range(5):
				print("------")
				for i in range(3):
					printColour = random.choice(a_Colours)
					print(f'{printColour}      {cC.reset}')
			print("------")

		elif ";clr" in s_userInput: # clear screen . . .
			for x in range(50):
				print("\n")

		elif ";die" in s_userInput: # exit console . . .
			b_running = False
			break

		else: # not a valid command . . .
			#print("'" + s_userInput + "' is not a valid command. \n")
			print(f"{cC.b_RED} \'{s_userInput}\' is not a valid command. \n")




	#elif :
		#

	else:  # Move files to created fold named with the extention . . .
		s_userInput = s_userInput.lower()
		if not glob.glob("*." + s_userInput) and len(s_userInput) > 0: # if cannot find file extention . . .
			print(f"{cC.b_RED} There are no \'.{s_userInput}\' files in this directory. \n {cC.reset}")

		elif glob.glob("*." + s_userInput): # if can find file extention . . .
			if os.path.isdir(s_fileDestination):  # Check if folder already exists . . .
				#print(cC.b_RED + "Folder already exists." + cC.reset)
				moveFiles()

			else:
				print(f"{cC.b_GREEN} Creating folder . . . {cC.reset}")
				os.makedirs(s_userInput)
				moveFiles()
			print(f"{cC.b_GREEN} COMPLETED {cC.reset}")











# old version . . . v1.0
"""
import os
import sys
import glob
import ctypes
import shutil
import colourCodes as cC

ctypes.windll.kernel32.SetConsoleTitleW("Simple clean up tool. | ScT - v1.0") # Window title

b_running = True
s_userInput = "xxxxxxxxxxxxxxx"
s_fileDestination = "xxxxxxxxxxxxxxx"
s_inputDisplayText = f"{cC.b_MAGENTA} > {cC.b_CYAN}"

# Default console colours
w_Foreground = cC.b_WHITE
w_Background = cC.b_BLACK_b

# Set up ansi
os.system('mode con: cols=115 lines=30') # set size of console . . .
os.system("CLS")
print(f"{cC.b_CYAN}{cC.b_GREEN_b}Created by: Matthew. Klatt{cC.reset}")
print(f"{cC.b_YELLOW} Type ';help' if needed. \n {cC.reset}")


# Define functions #################################################################
def moveFiles():
	print(f"{cC.b_GREEN} Moving folder . . . {cC.reset}")
	for file in sourcefiles:
		if file.endswith('.' + s_userInput):
			shutil.move(os.path.join(dir, file), os.path.join(s_fileDestination, file))

def colourReset():
	print(f"{w_Foreground} {w_Background}"); os.system("CLS")

####################################################################################














while b_running:
	dir = os.getcwd() # current dir . . .
	sourcefiles = os.listdir()
	print(cC.b_WHITE + dir)

	# Get input . . . #############################################################
	s_userInput = str(input(s_inputDisplayText).lower())
	s_userInput = s_userInput.replace('.', '')
	s_userInput = s_userInput.replace(' ', '')
	s_fileDestination = dir + "\\" + s_userInput
	print(f"{cC.reset}")

	# User commands . . .
	if s_userInput == ";die": # Kill program . . .
		b_running = False; break

	elif s_userInput == ";colres": # Reset colours in window (DEBUG)
		colourReset()

	elif s_userInput == ";cd":
		s_userInput = str(input("Enter path or directory. EG: 'C:\\Temp' | ;exit will cancel. " + s_inputDisplayText))
		print(cC.reset)
		if s_userInput == ";exit":
			# Do nothing
			print("")
		elif os.path.isdir(s_userInput):  # Check if dir or path the user wants to move to actually exists . . .
			os.chdir(s_userInput)
		else:
			print(cC.b_RED + "Could not find that directory, please check spelling. \n" + cC.reset)

	elif s_userInput == ";clr": # Clear screen . . .
		os.system("CLS")

	elif s_userInput == ";mkdir": # Create directory . . .
		s_userInput = str(input(f"Enter name for new folder. EG: 'C:\\Temp' | ;exit will cancel. {s_inputDisplayText}"))
		print(f"{cC.reset}")
		if s_userInput == ";exit":
			# Do nothing
			print("")

		elif not os.path.isdir(s_userInput):
				print(f"{cC.b_GREEN} Creating folder . . . {cC.reset}")
				os.makedirs(s_userInput)
		else:
			print(f"{cC.b_RED} Folder already exists. {cC.reset}")

	elif s_userInput == ";dir": # List files and folders in directory with colour . . .
		for entry in os.scandir("."):
			if entry.is_file():
				print(cC.YELLOW + entry.name + cC.reset)
			else:
				print(cC.MAGENTA + entry.name + cC.reset)
		print("\n")

	elif s_userInput == ";help":
		print(f"{cC.b_YELLOW}" ) #+ "To close the program, you can either . . .\n 1] Type ';die' into the input box.\n 2] Pressing CTRL+C on your keyboard. \n 3] Left click on the big X in the top right corner of the program window.\n")
		print(f";clr will clear the console window. \n")
		print(f";cd will let you change your working directory. \n")
		print(f";dir will list all files in the current directory. \n")
		print(f";help will show these messages again. \n\n")
		print(f"To move files with a certian extention, simply type what you wish to move. EG: .txt\n will move all .txt file to a folder named txt.\n {cC.reset}")
	#--------------------------------------------------------












	elif not glob.glob("*." + s_userInput): # if cannot find file extention . . .
		print(cC.b_RED + "There are no '." + s_userInput + "' files in this directory. \n" + cC.reset)

	elif glob.glob("*." + s_userInput): # if can find file extention . . .
		if os.path.isdir(s_fileDestination):  # Check if folder already exists . . .
			#print(cC.b_RED + "Folder already exists." + cC.reset)
			moveFiles()

		else:
			print(f"{cC.b_GREEN} Creating folder . . . {cC.reset}")
			os.makedirs(s_userInput)
			moveFiles()
		print(f"{cC.b_GREEN} COMPLETED {cC.reset}")
"""
