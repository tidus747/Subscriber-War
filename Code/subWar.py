#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#####################################LICENCE###################################
# Copyright (c) 2016 Faissal Bensefia
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
###############################################################################

import requests
import json
import curses
import random
import RPi_I2C_driver as I2C_LCD_driver
import time


# Read in the API key from api_key.txt
try:
    with open("apiKey.txt", "r") as file:
        APIKEY = file.readline().strip()
        if len(APIKEY) == 0:
            print("Please place your YouTube API key in api_key.txt")
            exit()
except FileNotFoundError:
    open("apiKey.txt", "w").close()
    print("Please place your YouTube API key in api_key.txt")
    exit()

# Aquires the number of subscribers a given channelID has
def getSubs(channelName):
    lastRequest = requests.get(
        "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" +
        channelName + "&key=" + APIKEY)
    return int(json.loads(lastRequest.text)["items"][0]["statistics"]["subscriberCount"])

playerNames = "ND"
playerSubCounts = 0
channelNames = "ND"

# Adds a user to be tracked
def addUser(displayName, channelName):
    global playerNames
    global playerSubCounts
    playerNames = displayName
    global channelNames
    channelNames = channelName
    playerSubCounts = 0

addUser("Piensa 3D", "ivantraceur8")
mylcd = I2C_LCD_driver.lcd()
mylcd.lcd_display_string("Suscriptores:", 1)

while True:
    try:
        playerSubCounts = getSubs(channelNames)
    except:
        pass  # If we can't get subcount at this time we'll just leave the value as it is


    mylcd.lcd_display_string(playerNames +' '+str(playerSubCounts), 2)
    mylcd.lcd_display_string("Hora: %s" %time.strftime("%H:%M:%S"), 3)
    mylcd.lcd_display_string("Dia: %s" %time.strftime("%d/%m/%Y"), 4)

endwin()
