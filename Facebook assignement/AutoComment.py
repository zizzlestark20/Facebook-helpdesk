import pyautogui as bot
# PyAutoGUI lets the current Python scripts control the mouse and keyboard to automate interactions with other applications.
import time
# time for giving proper breaks between each message
comments = [
    "Hi this is a bot!",
    "Commenting for a better reach!",
    "Checking the Auto comment bot",
    "Not meant to harm anyone",
    "Keep coding :P",
    "Keep your calm",
    "python brings magic!",
    "I am a programmer trying to figure out things",
    "found!",
    "Are you a coder?",
    "See ya in the battleground"
]

url = "https://www.facebook.com/20531316728/posts/10154009990506729/"
# this is an exapmle url

time.sleep(8)
# you have 8 second time to go to a URL and click on the comment box
for comment in range(20):
    bot.typewrite(comments[comment%11])
    bot.typewrite("\n")
    time.sleep(3)