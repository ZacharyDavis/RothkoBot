# Rothko_Bot

This bot creates images using the Python Imaging Library. These images are visually similar to the works of abstract artist Mark Rothko (1903-1970). 
Follow Rothko_Bot on Twitter! https://twitter.com/Rothko_Bot

The conversion methods from hex to RGB and the file containing the color selections are from here: https://github.com/joemfox/colorschemer

## Usage
If you would like to use this bot for your own Twitter account, follow these steps:

1. Install python via your favorite package manager
2. Install pip with `sudo easy_install pip`
3. Install tweepy with `pip install tweepy`
4. Install Pillow with `pip install Pillow`
4. Create a Twitter application here https://apps.twitter.com
5. Include your own API and Access keys in the .py file (found on the site above)
6. Run `python RothkoBot.py`

The source code is customizable to your own wants or needs. Any additions built upon the Python Imaging Library should work just fine!

## Examples of Rothko_Bot's Creations
![alt text](https://github.com/ZacharyDavis/RothkoBot/blob/master/Images/Rothko.gif)

## Problems Solved (or Circumvented)
- Implemented a running count of how many images have been tweeted out by Rothko_Bot. This was done using an external text file to keep track of the current tweet number to be loaded into the program when it is re-run after being terminated. Not the most elegant solution I'm sure, but it works...

This project is licensed under the terms of the MIT license.
