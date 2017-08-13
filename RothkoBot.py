#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, os, math, random, struct, string
from PIL import Image, ImageDraw


# Enter the corresponding information from your Twitter application:
CONSUMER_KEY = os.environ['ROTHKO_API_KEY']        # Replace this with your consumer key or set an environmental variable
CONSUMER_SECRET = os.environ['ROTHKO_API_SECRET']  # Replace this with your consumer secret key or set an environmental variable
ACCESS_KEY = os.environ['ROTHKO_ACCESS_TOKEN']     # Replace this with your access token or set an environmental variable
ACCESS_SECRET = os.environ['ROTHKO_ACCESS_SECRET'] # Replace this with your access token secret or set and environmental variable
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

color = open("colors.txt", "r") 
colors = color.read().splitlines()
color.close()

while True:
	fourcolors = False
	color1 = colors[random.randint(0,len(colors)-1)].split(",") # Select background color and name
	color2 = colors[random.randint(0,len(colors)-1)].split(",") # Select first rectangle color and name
	color3 = colors[random.randint(0,len(colors)-1)].split(",") # Select second rectangle color and name
	color4 = colors[random.randint(0,len(colors)-1)].split(",") # Secelect third rectangle color and name

	colorstr1 = struct.unpack("BBB",color1[1][1:].decode("hex")) # Decode hex color values to (R,G,B) format 
	colorstr2 = struct.unpack("BBB",color2[1][1:].decode("hex"))
	colorstr3 = struct.unpack("BBB",color3[1][1:].decode("hex"))
	colorstr4 = struct.unpack("BBB",color4[1][1:].decode("hex"))

	WIDTH,HEIGHT = 418,518

	length1 = random.randint(10,278)  # Determine lengths of each rectangle
	length2 = random.randint(0,(478-length1))
	length3 = 463-(length2+length1)

	RothkoImage = Image.new('RGB', (WIDTH, HEIGHT))
	draw = ImageDraw.Draw(RothkoImage)
	draw.rectangle([0, 0, WIDTH, HEIGHT], fill=colorstr1, outline=colorstr1)
	draw.rectangle([20, 20, WIDTH-20, length1+20], fill=colorstr2, outline=colorstr2)
	draw.rectangle([20, length1+30, WIDTH-20, length2+length1+30], fill=colorstr3, outline=colorstr3)
	if length3 > 0:
		draw.rectangle([20, length1+length2+40, WIDTH-20, length1+length2+length3+40], fill=colorstr4, outline=colorstr4)
		fourcolors = True

	RothkoPng = "Rothko.png"
	RothkoImage.save(RothkoPng)

	if fourcolors:
		tweet = color2[0].title() + ", " + color3[0].title() + ", and " + color4[0].title() + " on " + color1[0].title()
	else:
		tweet = color2[0].title() + " and " + color3[0].title() + " on " + color1[0].title()
	
	api.update_with_media(RothkoPng, tweet) # Send tweet
	time.sleep(5400) # Wait 2  hours before tweeting again

