#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy, time, sys, os, math, random, struct, string
from PIL import Image, ImageDraw, ImageFilter

# Implementing 'touch' command functionality to create a location for the PNG to be stored
def touch(fname, times=None):
    with open(fname, 'a'):
        os.utime(fname, times)

# Function to retrieve current tweet number from local file in case of program termination.
def get_tweet_count():
    tweet_count = open("tweet_count.txt", "r")
    tweet_num = int(tweet_count.read())
    tweet_count.close()
    return tweet_num

# Function to save the image that is to be tweeted and return the path of the image
def save_image(tweet_number, image):
    image_filename = "Rothko"+str(tweet_number)+".png"
    image_path = os.getcwd()+"/Images/"+image_filename
    touch(image_path)
    image.save(image_path)
    return image_path

# Boilerplate code for using the Twitter API
# Enter the corresponding information from your Twitter application:
CONSUMER_KEY = os.environ['ROTHKO_API_KEY']        # Replace this with your consumer key or set an environmental variable
CONSUMER_SECRET = os.environ['ROTHKO_API_SECRET']  # Replace this with your consumer secret key or set an environmental variable
ACCESS_KEY = os.environ['ROTHKO_ACCESS_TOKEN']     # Replace this with your access token or set an environmental variable
ACCESS_SECRET = os.environ['ROTHKO_ACCESS_SECRET'] # Replace this with your access token secret or set and environmental variable
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

color_file = open("colors.txt", "r") 
colors = color_file.read().splitlines()
color_file.close()

tweet_number = get_tweet_count()

while True:
    four_colors = False
    color1 = colors[random.randint(0,len(colors)-1)].split(",") # Select background color and name
    color2 = colors[random.randint(0,len(colors)-1)].split(",") # Select first rectangle color and name
    color3 = colors[random.randint(0,len(colors)-1)].split(",") # Select second rectangle color and name
    color4 = colors[random.randint(0,len(colors)-1)].split(",") # Secelect third rectangle color and name
    
    color_str1 = struct.unpack("BBB",color1[1][1:].decode("hex")) # Decode hex color values to (R,G,B) format 
    color_str2 = struct.unpack("BBB",color2[1][1:].decode("hex"))
    color_str3 = struct.unpack("BBB",color3[1][1:].decode("hex"))
    color_str4 = struct.unpack("BBB",color4[1][1:].decode("hex"))
    
    WIDTH,HEIGHT = 418,518
    length1 = random.randint(10,278)  # Determine lengths of each rectangle
    length2 = random.randint(0,(478-length1))
    length3 = 463-(length2+length1)
    
    rothko_image = Image.new('RGB', (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(rothko_image)
    draw.rectangle([0, 0, WIDTH, HEIGHT], fill=color_str1, outline=color_str1)
    draw.rectangle([20, 20, WIDTH-20, length1+20], fill=color_str2, outline=color_str2)
    draw.rectangle([20, length1+30, WIDTH-20, length2+length1+30], fill=color_str3, outline=color_str3)
    
    if length3 > 0:
        draw.rectangle([20, length1+length2+40, WIDTH-20, length1+length2+length3+40], fill=color_str4, outline=color_str4)
        four_colors = True

    rothko_path = save_image(tweet_number, rothko_image)

    if four_colors:
        tweet = "No. " + str(tweet_number) + " (" + color2[0].title() + ", " + color3[0].title() + ", and " + color4[0].title() + " on " + color1[0].title() + ")"
        tweet_number = tweet_number + 1
    else:
        tweet = "No. " + str(tweet_number) + " (" + color2[0].title() + " and " + color3[0].title() + " on " + color1[0].title() + ")"   
        tweet_number = tweet_number + 1

    # Write current tweet count to file in case of termination
    tweet_count = open("tweet_count.txt", "w")
    tweet_count.write(str(tweet_number))
    tweet_count.close()

    api.update_with_media(rothko_path, tweet) # Send tweet
    time.sleep(7200) # Wait 2 hours before tweeting again
