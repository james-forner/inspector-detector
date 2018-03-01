#!/usr/bin/env python2

import string
import random

from firebase import firebase

firebase = firebase.FirebaseApplication('https://inspector-detector.firebaseio.com/', None)

def generateKey(size=8):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(size))
    
UNIQUE_KEY = generateKey(8)
i=0

FIXED_KEY_DEVICE = "DEVICE1"
FIXED_KEY_CLIENT = "CLIENT1"

valid_commands = ['send', 'shutdown', 'close', 'reboot']

working = True

def send_command(var=""):
    COMMAND_DIR = ("/" + FIXED_KEY_DEVICE + "/commands");
    firebase.post(COMMAND_DIR, var)
    
    
while working:
    
    command = raw_input("Enter command: ")
    command = command.lower()
    
    if command == "exit":
        working = False
        break
    
    if  command in valid_commands:
        send_command(command)
    else:
        print("Invalid command. Try again.")


print("Program ending...")
