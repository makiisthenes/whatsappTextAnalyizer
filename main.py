# C:\Users\Michael\Documents\Coding Projects\Python PROJECTS\Random Python Projects\Trackers Software\Whatsapp Analysis\data\test.txt

# C:\Users\Michael\Documents\Coding Projects\Python PROJECTS\Random Python Projects\Trackers Software\Whatsapp Analysis\data\test_total.txt

#  _    _ _           _                            ___              _       _
# | |  | | |         | |                          / _ \            | |     (_)
# | |  | | |__   __ _| |_ ___  __ _ _ __  _ __   / /_\ \_ __   __ _| |_   _ _ _______ _ __
# | |/\| | '_ \ / _` | __/ __|/ _` | '_ \| '_ \  |  _  | '_ \ / _` | | | | | |_  / _ \ '__|
# \  /\  / | | | (_| | |_\__ \ (_| | |_) | |_) | | | | | | | | (_| | | |_| | |/ /  __/ |
#  \/  \/|_| |_|\__,_|\__|___/\__,_| .__/| .__/  \_| |_/_| |_|\__,_|_|\__, |_/___\___|_|
#                                  | |   | |                           __/ |
#                                  |_|   |_|                          |___/			BY Michael Peres.

import os
import datetime
import emoji
from collections import Counter
import string
from time import sleep
# import matplotlib
# import numpy as np
# import matplotlib.pyplot as plt

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

alpha_list = ['-', ':', '/', '.', '?', '!', "'", '"', '^', '(', ')', 'π', ' ', ',', ']', '[', '<', '>', r'\\', '', '  ',
			  '   ', '    ', '*', '+', '-', '\\']
for x in string.ascii_uppercase:
	alpha_list.append(x)
for x in string.ascii_lowercase:
	alpha_list.append(x)
for x in string.digits:
	alpha_list.append(x)
usr_input = ''
files = []

# could implement the use of objects to name dates. attributes like message number...
# main things: adding time difference between messages and what emoji was sent...
emoji_input = ''
usera_emoji_list = []
userb_emoji_list = []
users = []
erafer = 0
hasChosen = False
topUsedEmojiX = None
topUsedEmojiY = None


# problem with the dictionary of spelling is that, it makes the program really slow, 4 seconds each message,
# so i want to make it more easier...
# splitting the dictionary by thier letter each in order to increase performance.


def eng_analysis(eng_word, user):  # to be continued, will add spell checking, add user parameter.
	global userx_spelling_mistakecount
	global usery_spelling_mistakecount
	if user == 'userx':  # links message to this userx
		pass
	if user == 'usery':  # links message to this userx
		pass
	exit_loop = False
	len_eng_word = len(eng_word)
	# we also need a parameter for who this text belongs to.
	cd_path = os.getcwd() + r'\langAnalysis\savefile'+eng_word[0].upper()+'_PATH.txt'
	# this will look at file containing the first letter of this word, to improve speed
	# finds the directory the script is running from
	with open(cd_path, encoding="utf8") as eng_file:
		for eng_word_check in eng_file:
			if eng_word_check == eng_word:
				exit_loop = True
				# meaning the word is in the dictionary and working.
				pass
			if not exit_loop:
				# meaning the word was not found.
				for eng_word_characters in range(len_eng_word):
					try:
						if eng_word[eng_word_characters] == eng_word_check[eng_word_characters]:
							pass
						# go and check the next letter
						# i want an accuracy of 80% before we tell them the user meant this word.
						else:
							pass
						# skip this word in the dictionary and check the next one...
					except IndexError:
						pass
					# please look to see if this exception allows analysis
			if exit_loop:
				exit_loop = False  # getting out of the for loop.
				pass
	# accessing the words one by one, need to find a link...
	# we want to check whether this word is include in the dictionary or its spelled wrong..


def get_users():
	global textfile
	global usera
	global userb
	hasError = False
	hasFound = False
	# TRY EXCEPTION FOR NO FILE FOUND ERROR...
	while not hasFound:
		textfile = input('Enter the file PATH of export for parameters set:: ')
		try:
			with open(textfile, encoding="utf8") as openfile:
				for line in openfile:
					if line[0] not in numbers:  # date-line verifying.
						hasError = True
					if not hasError:
						erafer = 0
						# print(line)
						for part in line.split():
							# print('part count' + str(part_count))
							if erafer == 3:
								if part not in users:
									if part != 'Messages':
										users.append(part)
							erafer = erafer + 1
			usera = users[0]
			userb = users[1]
			# print(usera)
			# print(userb)
			hasFound = True
		except OSError:
			print('Path was not found make sure there is not spaces. And try again..')


def emoji_search_x(emoji_input):
	global topUsedEmojiX
	global userb_emoji_list
	for emoji_namex, emoji_textx in emoji.EMOJI_UNICODE.items():
		if emoji_textx == emoji_input:
			# print(userb_name + ' sent the emoji '+emoji_namex)
			userb_emoji_list.append(emoji_namex)
	topUsedEmojiX = Counter(userb_emoji_list).most_common(5)


def emoji_search_y(emoji_input):
	global topUsedEmojiY
	global usera_emoji_list
	# emoji_namey is the name given to the emoji character for user y
	# emoji_text is emoji character that is linked to that emoji_namey.
	for emoji_namey, emoji_texty in emoji.EMOJI_UNICODE.items():  # here we meed to check the whole dictionary to see if
		if emoji_texty == emoji_input:
			# print(usera_name + ' sent the emoji '+ emoji.demojize(emoji_input))
			emoji_name = emoji.demojize(emoji_input)
			usera_emoji_list.append(emoji_name)
	topUsedEmojiY = Counter(usera_emoji_list).most_common(5)
# later give option for seeing x number of top emojis used...


def analyize_txt(textfile):
	global z_state
	global m_state
	global o_emoji
	global t_message
	global rat
	global hasCompleted
	global userb_emoji
	global usera_emoji
	global print1
	global print2
	global print3
	global print4
	global print5
	global print6
	global print7
	global print8
	global print9
	global print10
	global print11
	global print12
	global print13

	line = 0
	date = ''
	x = 0
	y = 0
	z = 0
	images = 0
	images_y = 0
	images_x = 0
	emoji_count = 0
	emoji_count_x = 0
	emoji_count_y = 0
	unqiue_count = []
	part_count = 0
	line_part_count = 0
	# day_line_count = 0
	init_x = 0
	init_y = 0
	user1EmojiCount = {}
	user2EmojiCount = {}
	belongsUserB = False
	belongsUserA = False
	message_contents = []
	part4checker = False
	with open(textfile, encoding="utf8") as openfile:
		if showText:
			print('''
				+-------------------------------------Texts-------------------------------------+
				''')
		for line in openfile:
			line_total_part_counter = int(len(line.split())) - 1  # maximum part_count of message...
			hasError = False
			if line[0] not in numbers:  # date-line verifying.
				hasError = True
			if not hasError:
				line_part_count = line_part_count + 1
				for date_check in line.split():
					if date_check not in unqiue_count:  # unique count being the new days...
						part_count = 0
				for part in line.split():  # go through the words in the specific line.
					# print(str(part_count) + ' ' + str(part))
					# print(line)
					# print(part)
					if part_count == 0:  # checking the data of message
						userx = False
						usery = False
						new_part = part.replace(',', '')
						date = new_part
						if date not in unqiue_count:
							unqiue_count.append(date)
							line_part_count = 0
							if showText:
								print('These messages were sent on ' + date + ':')
					# this will find the unqiue date stamp for this information...
					# print('part count '+ str(line_part_count))
					if part_count == 1:
						msg_time = part  # this is time stamp of message...
						if showText:
							print(
								'This message was sent at ' + msg_time)  # want to add time difference before each message...
							print('	--> ' + line)
					if userb in part:
						x = x + 1
						userx = True  # serialising this message to belong to this individual.
					elif usera in part:
						y = y + 1
						usery = True
					for letters in part:
						if letters in emoji.UNICODE_EMOJI:  # place where individual letters are seen if emojis exsist...
							emoji_count = emoji_count + 1
							for emoji_link_checker in line.split():
								if userb in emoji_link_checker:
									emoji_count_x = emoji_count_x + 1  # user 1 emoji count...
									belongsUserA = True
								elif usera in emoji_link_checker:
									emoji_count_y = emoji_count_y + 1  # user 2 emoji count...
									belongsUserB = True
						if belongsUserB:
							emoji_search_x(letters)
							belongsUserB = False
						elif belongsUserA:
							emoji_search_y(letters)
							belongsUserA = False
					# adding the actual text sent in the message container..
					# the part count at which the comment starts is when name':' is found. DONE
					# the message ends at when part_count  = 0, or quality check, or 11 characters, with 6 numbers, 3 /
					if part_count == 3:
						# this is suppose to be the name of user, unless there is a space in the name.
						check_name = part
						if check_name.__contains__(':'):
							message_start = int(part_count) + 1
						else:
							part4checker = True
					if part_count == 4 and part4checker:
						check_name = part
						if check_name.__contains__(':'):
							message_start = int(part_count) + 1
							part4checker = False
						else:
							print('Please change the name of user, because we cannot determine message start...')
							exit()
					# message_start will be on part_count 5 or 6 depending on the user's name..
					# need a way to determine when the message ends on this line.
					if devOption:
						if part_count >= 4 and message_start == 4:
							# this is where message starts. the part count will automatically reset to 0 when new line is reached
							if part != 'omitted>' or '<Media':
								message_contents.append(part)
							if userx:
								user = 'userx'
							elif usery:
								user = 'usery'
							# quality check to make sure
							# this list is going to be analysed, word be word...
							for word_contents in message_contents:
								# check dictionary of words json file...
								eng_analysis(word_contents, user)
					if devOption:
						if part_count >= 5 and message_start == 5:
							# this is where message starts. the part count will automatically reset to 0 when new line is reached
							# needs to be moved to when message is line part resets to 0;
							if part != 'omitted>' or '<Media':
								message_contents.append(part)
							if userx:
								user = 'userx'
							elif usery:
								user = 'usery'
							for word_contents in message_contents:  # this list is going to be analysed, word be word...
								eng_analysis(word_contents, user)
								# we also need a parameter for who this text belongs to.
								# check dictionary of words json file...
								pass
						if part_count == line_total_part_counter:
							# at the end of the message the list is reset back to initial.
							message_contents = []

					if '<Media' in part:
						images = images + 1
						# print(line)
						for subpart in line.split():
							# this will print the full line to '<Media'
							# print(subpart)
							if userb in subpart:
								images_x = images_x + 1
							elif usera in subpart:
								images_y = images_y + 1
					part_count = part_count + 1  # new word, loop ends here for loop analysis.
				if line_part_count == 0:  # initiated user checker
					for init_checker in line.split():
						if userb in init_checker:
							init_x = init_x + 1
						elif usera in init_checker:
							init_y = init_y + 1
	print('''
	+-------------------------------------Analysis-------------------------------------+
	''')

	# need to make this one big print statement to be able to send to an text file...
	print('--> ' + userb_name + ' has sent total: ' + str(x) + ' messages.')
	z_state = userb_name + ' has sent total: ' + str(x) + ' messages.'
	print('--> ' + usera_name + ' has sent total: ' + str(y) + ' messages.')
	m_state = usera_name + ' has sent total: ' + str(y) + ' messages.'
	print('--> Overall emoji count: {}'.format(str(emoji_count)))
	o_emoji = 'Overall emoji count: {}'.format(str(emoji_count))
	print('--> ' + userb_name + ' number of emojis send:: ' + str(emoji_count_x) + '.')
	userb_emoji = '--> ' + userb_name + ' number of emojis send:: ' + str(emoji_count_x) + '.'
	print('--> ' + usera_name + ' number of emojis send:: ' + str(emoji_count_y) + '.')
	usera_emoji = '--> ' + usera_name + ' number of emojis send:: ' + str(emoji_count_y) + '.'
	print('--> The number of images/stickers send on this day is: ' + str(images) + '.')
	print1 = '--> The number of images/stickers send on this day is: ' + str(images) + '.'
	print('--> ' + usera_name + ' sticker/ picture sent:: ' + str(images_y) + ' stickers.')
	print2 = '--> ' + usera_name + ' sticker/ picture sent:: ' + str(images_y) + ' stickers.'
	print('--> ' + userb_name + ' sticker/ picture sent:: ' + str(images_x) + ' stickers.')
	print3 = '--> ' + userb_name + ' sticker/ picture sent:: ' + str(images_x) + ' stickers.'
	print('--> ' + usera_name + ' actual message sent:: ' + str(y - images_y) + '.')
	print4 = '--> ' + usera_name + ' actual message sent:: ' + str(y - images_y) + '.'
	print('--> ' + userb_name + ' actual message sent:: ' + str(x - images_x) + '.')
	print5 = '--> ' + userb_name + ' actual message sent:: ' + str(x - images_x) + '.'
	print('--> Total Messages: ' + str(int(y) + int(x)) + ' messages send on ' + date + '[total].')
	t_message = 'Total Messages: ' + str(int(y) + int(x)) + ' messages send on ' + date + '[total].'
	word = int(y) + int(x)
	try:
		rat_eng = float((float(x) / float(word))) * 100
	except ZeroDivisionError:
		rat_eng = 'ERROR'
	rat = '--> Ratio of Engagement: {}% for all data.'.format(rat_eng)
	print(rat)
	word = int(y - images_y) + int(x - images_x)
	try:
		rat_eng_actual = float((float(x - images_x) / float(word))) * 100
	except ZeroDivisionError:
		rat_eng_actual = 'ERROR'
	print('--> Ratio of Actual Engagement: {}% for text messages.'.format(rat_eng_actual))
	print6 = '--> Ratio of Actual Engagement: {}% for text messages.'.format(rat_eng_actual)
	print("--> Dates of data used " + str(unqiue_count) + '.')
	print7 = "--> Dates of data used " + str(unqiue_count) + '.'
	print("--> No of days of data used:: " + str(len(unqiue_count)) + ' days.')
	print8 = "--> No of days of data used:: " + str(len(unqiue_count)) + ' days.'
	print('--> Number of times ' + userb_name + ' has initiated: ' + str(init_x) + ' time(s).')
	print9 = '--> Number of times ' + userb_name + ' has initiated: ' + str(init_x) + ' time(s).'
	print('--> Number of times ' + usera_name + ' has initiated: ' + str(init_y) + ' time(s).')
	print10 = '--> Number of times ' + usera_name + ' has initiated: ' + str(init_y) + ' time(s).'
	print('--> The users in this conversation is ' + usera_name + ' and ' + userb_name + '.')
	print11 = '--> The users in this conversation is ' + usera_name + ' and ' + userb_name + '.'
	print('The top 5 most used emojis by ' + userb_name + ' are ' + str(topUsedEmojiX))
	print12 = 'The top 5 most used emojis by ' + userb_name + ' are ' + str(topUsedEmojiX)
	print('The top 5 most used emojis by ' + usera_name + ' are ' + str(topUsedEmojiY))
	print13 = 'The top 5 most used emojis by ' + usera_name + ' are ' + str(topUsedEmojiY)
	# print(userb_emoji_list)
	# print(usera_emoji_list)
	print('''
	
	''')
	print('''
	+----------------------------------------END---------------------------------------+
	''')
	hasCompleted = True


def savefile():
	file_path_save = os.getcwd() + r'\logfile.txt'  # connect a '\logfile.txt' to the directory...
	with open(file_path_save, 'w') as savefile:
		savefile.write(str(z_state) + '\n')
		savefile.write(str(m_state) + '\n')
		savefile.write(str(o_emoji) + '\n')
		savefile.write(str(userb_emoji) + '\n')
		savefile.write(str(usera_emoji) + '\n')
		savefile.write(str(print1) + '\n')
		savefile.write(str(print2) + '\n')
		savefile.write(str(print3) + '\n')
		savefile.write(str(print4) + '\n')
		savefile.write(str(print5) + '\n')
		savefile.write(str(print6) + '\n')
		savefile.write(str(print7) + '\n')
		savefile.write(str(print8) + '\n')
		savefile.write(str(print9) + '\n')
		savefile.write(str(print10) + '\n')
		savefile.write(str(print11) + '\n')
		savefile.write(str(print12) + '\n')
		savefile.write(str(print13) + '\n')
	savefile.close()
	return 'The log file has been created and saved in directory'


def list_files():
	for f in os.walk(os.getcwd()):
		for file in f:
			if '.txt' in file:
				files.append(os.path.join(f, file))
		for names in files:
			print(names)


print('Please be aware selecting (Y) is unstable and may not work...')
user_opt1 = input('Do you want to see the texts[live] during analysis::: (Y)es or (N)o:: ').upper()
while True:
	if user_opt1 == 'Y':
		showText = True
		break
	elif user_opt1 == 'N':
		showText = False
		break
	else:
		user_opt1 = input('Do you want to see the texts[live] during analysis::: (Y)es or (N)o:: ').upper()
get_users()
usera_name = usera.replace(':', '')
# print(usera)
userb_name = userb.replace(':', '')
# print(userb)
hasCompleted = False
while usr_input != 1 and not hasCompleted:
	print("To analyse the WhatsApp texts today, continue, else write 'EXIT' to exit program")
	try:
		try:
			dev_opt = input('To enable BETA spelling mode, type "ENABLE" or press anything to continue... [DONT ENABLE]').upper()
			print('This mode goes through 300 thousand words for each word in the message, takes a long time to complete.')
			if dev_opt == 'ENABLE':
				devOption = True
			else:
				devOption = False
			analyize_txt(textfile)
			while not hasChosen:
				opt2 = input('Do you want a log file of this analysis:: (Y)es or (N)o:: ').upper()
				if opt2 == 'Y':
					savefile()
					print('The log file has been created and saved in directory')
					sleep(1)
					hasChosen = True
				elif opt2 == 'N':
					print('You have chosen to not save this...')
					sleep(1)
					hasChosen = True
				else:
					print('Not a valid response...')
					sleep(0.5)
			if usr_input == 'HELP':
				list_files()
		except FileNotFoundError:
			if usr_input == 'HELP':
				list_files()
			else:
				print('Path was not found, please try again... FileNotFoundError')
	except OSError:
		print('Path was not found, please try again... OSError')
