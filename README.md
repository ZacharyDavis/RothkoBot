# Rothko_Bot

This bot creates images using PIL that are visually similar to the works of artist Mark Rothko. 
Be sure to follow Rothko_Bot on Twitter! https://twitter.com/Rothko_Bot

The conversion methods from hex to RGB and the file containing the color selections are from here: https://github.com/joemfox/colorschemer

## Usage
If you would like to use this bot for your own Twitter acount, follow these steps:

1. Install python via your favorite package manager
2. Install pip with `sudo easy_install pip`
3. Install tweepy with `pip install tweepy`
4. Install Pillow with `pip install Pillow`
4. Create a Twitter application here https://apps.twitter.com
5. Include your own API and Access keys in the .py file (found on the site above)
6. Run `python RothkoBot.py`

The source code is very customizable and has many capabilites using the PIL library.

## Examples of Rothko_Bot's Creations
![alt text](https://github.com/ZacharyDavis/RothkoBot/blob/master/Images/Rothko2989.png)
![alt text](https://github.com/ZacharyDavis/RothkoBot/blob/master/Images/Rothko2988.png)
![alt text](https://github.com/ZacharyDavis/RothkoBot/blob/master/Images/Rothko2974.png)
![alt text](https://github.com/ZacharyDavis/RothkoBot/blob/master/Images/Rothko2972.png)

## Problems Solved (or Circumvented)
- Implemented a running count of how many images have been tweeted out by Rothko_Bot. This was done using an external text file to keep track between between program termination and recompile. Not the most elegant solution I'm sure, but it works...

This project is licensed under the terms of the MIT license.
