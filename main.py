# C:\Users\Michael\Documents\Coding Projects\Python PROJECTS\Random Python Projects\Trackers Software\Whatsapp Analysis\data\test.txt

from emoji_names import emoji_names_x
from emoji_names import emoji_names_y
import string
import os
import datetime
import emoji
# import numpy as np
# import matplotlib.pyplot as plt  # Horizontal bar plot
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

alpha_list = ['-', ':', '/', '.', '?', '!', "'", '"', '^', '(', ')', 'π', ' ', ',', ']', '[', '<', '>', '\\', '', '  ', '   ', '    ', '*', '+', '-']
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

users = []
erafer = 0


def get_users():
	global textfile
	global usera
	global userb
	hasError = False
	textfile = input('Enter the file PATH of export for parameters set:: ')
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
							users.append(part)
					# print(part)
					erafer = erafer + 1
	usera = users[0]
	userb = users[1]


def emoji_counter():
	pass
	# need to make lists turn into dictionary


def emoji_search_x(emoji_input):
	for emoji_namex, emoji_text in emoji.EMOJI_UNICODE.items():
		if emoji_text == emoji_input:
			print(emoji_namex) # need to record this in something, make a new function.


def emoji_search_y(emoji_input):
	for emoji_namey, emoji_text in emoji.EMOJI_UNICODE.items():
		if emoji_text == emoji_input:
			print(emoji_namey) # need to record this in something, make a new function.


def analyize_txt(textfile):
	global z_state
	global m_state
	global o_emoji
	global t_message
	global rat
	global hasCompleted
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


	with open(textfile, encoding="utf8") as openfile:
		print('''
			+-------------------------------------Texts-------------------------------------+
			''')
		for line in openfile:
			hasError = False
			if line[0] not in numbers:  # date-line verifying.
				hasError = True
			if not hasError:
				line_part_count = line_part_count + 1
				for date_check in line.split():
					if date_check not in unqiue_count:
						part_count = 0
				for part in line.split():
					# print(str(part_count)+ ' ' + str(part))
					# print(line)
					# print(part)
					if part_count == 0:  # checking the data of message
						new_part = part.replace(',', '')
						date = new_part
						if date not in unqiue_count:
							unqiue_count.append(date)
							line_part_count = 0
							print('These messages were sent on ' + date + ':')
						# this will find the unqiue date stamp for this information...
					# print('part count '+ str(line_part_count))
					if part_count == 1:
						msg_time = part
						print('This message was sent at ' + msg_time) # want to add time difference before each message...
						print('	--> '+ line)
						# print(str(line_part_count) + ' ' + str(line))
					if userb in part:
						x = x + 1
					elif usera in part:
						y = y + 1
					for letters in part:
						if letters in emoji.UNICODE_EMOJI:
							emoji_count = emoji_count + 1
							for emoji_link_checker in line.split():
								if userb in emoji_link_checker:
									emoji_count_x = emoji_count_x + 1
									belongsUserA = True
								elif usera in emoji_link_checker:
									emoji_count_y = emoji_count_y + 1
									belongsUserB = True
						if belongsUserB:
							emoji_search_x(letters)
							belongsUserB = False
						elif belongsUserA:
							emoji_search_y(letters)
							belongsUserA = False
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
					part_count = part_count + 1
				if line_part_count == 0:
					for init_checker in line.split():
						if userb in init_checker:
							init_x = init_x + 1
						elif usera in init_checker:
							init_y = init_y + 1
	print('''
	+-------------------------------------Analysis-------------------------------------+
	''')
	print('--> '+userb_name+' has sent total: ' + str(x) + ' messages.')
	z_state = userb_name+' has sent total: ' + str(x) + ' messages.'
	print('--> '+usera_name+' has sent total: ' + str(y) + ' messages.')
	m_state = usera_name + ' has sent total: ' + str(y) + ' messages.'
	print('--> Overall emoji count: {}'.format(str(emoji_count)))
	o_emoji = 'Overall emoji count: {}'.format(str(emoji_count))
	print('--> '+userb_name+' number of emojis send:: '+ str(emoji_count_x)+'.')
	print('--> '+usera_name+' number of emojis send:: ' + str(emoji_count_y)+'.')
	print('--> The number of images/stickers send on this day is: ' + str(images) + '.')
	print('--> '+usera_name+' sticker/ picture sent:: ' + str(images_y) + ' stickers.')
	print('--> '+userb_name+' sticker/ picture sent:: ' + str(images_x) + ' stickers.')
	print('--> '+usera_name+' actual message sent:: ' + str(y - images_y)+'.')
	print('--> '+userb_name+' actual message sent:: ' + str(x - images_x)+'.')
	print('--> Total Messages: ' + str(int(y) + int(x)) + ' messages send on ' + date + '[total].')
	t_message = 'Total Messages: ' + str(int(y) + int(x)) + ' messages send on ' + date + '[total].'
	word = int(y) + int(x)
	try:
		rat_eng = float((float(x) / float(word))) * 100
	except ZeroDivisionError:
		rat_eng = 'ERROR'
	# print('Ratio of Engagement: {}% for all data'.format(rat_eng))
	rat = '--> Ratio of Engagement: {}% for all data.'.format(rat_eng)
	print(rat)
	word = int(y - images_y) + int(x - images_x)
	try:
		rat_eng_actual = float((float(x - images_x) / float(word))) * 100
	except ZeroDivisionError:
		rat_eng_actual = 'ERROR'
	print('--> Ratio of Actual Engagement: {}% for text messages.'.format(rat_eng_actual))
	print("--> Dates of data used "+ str(unqiue_count)+'.')
	print("--> No of days of data used:: " + str(len(unqiue_count))+' days.')
	print('--> Number of times '+userb_name+' has initiated: '+ str(init_x) + ' time(s).')
	print('--> Number of times '+usera_name+' has initiated: ' + str(init_y) + ' time(s).')
	print('''
	''')
	print('''
		+----------------------------------------END---------------------------------------+
		''')
	hasCompleted = True


def list_files():
	for f in os.walk(
			r'C:\Users\Michael\Documents\Coding Projects\Python PROJECTS\Random Python Projects\Whatsapp Analysis\chat_txt'):
		for file in f:
			if '.txt' in file:
				files.append(os.path.join(f, file))
		for names in files:
			print(names)


def date_file_labeller():
	global textname
	global dt
	dt = datetime.datetime.today()
	textname = str(dt.day) + '-' + str(dt.month) + 'textAnalysis.txt'
	print(textname)

get_users()
usera_name  = usera.replace(':', '')
# print(usera)
userb_name = userb.replace(':', '')
# print(userb)
hasCompleted = False
while usr_input != 1 and not hasCompleted:
	print("To analyise the WhatsApp texts today, continue, else write 'EXIT' to exit program")
	try:
		try:
			date_file_labeller()
			analyize_txt(str(textfile))
			if usr_input == 'HELP':
				list_files()
		except FileNotFoundError:
			if usr_input == 'HELP':
				list_files()
			else:
				print('Path was not found, please try again...')
	except OSError:
		print('Path was not found, please try again...')


