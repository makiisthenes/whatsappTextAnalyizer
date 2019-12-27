import os
import requests
import subprocess
from time import sleep


def check_connection():
	try:
		r = requests.get('https://www.google.com')
		hasConnection = True
		print('Connected to the internet')

	except requests.exceptions.ConnectionError:
		hasConnection = False
		print('Not connected to the internet')


proc = subprocess.Popen('cmd.exe', stdin = subprocess.PIPE, stdout = subprocess.PIPE)
# Given that you are using wifi connection this will work, with your using wlan0 you may have to refactor code.

def enable():
	os.system('ipconfig /renew WiFi')

	
def disable():
	os.system('ipconfig /release WiFi')

	
while True:
	sleep(0.5)
	usr = input('Type in D for disable, C for checking status and E for enabling wifi connection::').upper()
	if usr == 'D':
		disable()
	elif usr == 'E':
		enable()
	elif usr == 'C':
		check_connection()
	else:
		print('Input was not recognised, please try again...')

# Made by Michael Peres		
		
