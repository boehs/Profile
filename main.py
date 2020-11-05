import os
import time
import webbrowser
import random

# region: variables
name = r"""
      ___                                     ___     
     /  /\          ___          ___         /__/\    
    /  /:/_        /__/\        /__/\        \  \:\   
   /  /:/ /\       \  \:\       \  \:\        \  \:\  
  /  /:/ /:/_       \  \:\       \  \:\   _____\__\:\ 
 /__/:/ /:/ /\  ___  \__\:\  ___  \__\:\ /__/::::::::\
 \  \:\/:/ /:/ /__/\ |  |:| /__/\ |  |:| \  \:\~~\~~\/
  \  \::/ /:/  \  \:\|  |:| \  \:\|  |:|  \  \:\  ~~~ 
   \  \:\/:/    \  \:\__|:|  \  \:\__|:|   \  \:\     
    \  \::/      \__\::::/    \__\::::/     \  \:\    
     \__\/           ~~~~         ~~~~       \__\/    
"""
background = "\033[30;107m"
default = "\033[0m"
location = ""


# endregion

def launch():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(name)
    print(background + location + default)


# region: tld def
def art():
    global location
    location = r"bin\art"
    launch()
    while True:
        try:
            options = int(input("[1] Go Back \n"
                                "[2] Unspash \n"
                                "[Enter Choice]: "))
        except ValueError:
            launch()
        else:
            if options == 1:
                home()
                break
            elif options == 2:
                webbrowser.open("https://unsplash.com/@evvn")
            else:
                launch()


def projects():
    global location
    location = r"bin\projects"
    launch()
    while True:
        try:
            options = int(input("[1] Go Back \n"
                                "[2] See All Projects \n"
                                "[3] View Notable Projects \n"
                                "[Enter Choice]: "))
        except ValueError:
            launch()
        else:
            if options == 1:
                home()
                break
            elif options == 2:
                webbrowser.open("https://github.com/Scaledi")
            elif options == 3:
                niceProjects()
            else:
                launch()


def about():
    global location
    location = r"bin\about"
    launch()
    print("hi guys! I am evan, and I am so glad you are visiting my site! I code for a hobby, and one day a living, "
          "and am trying to make interesting stuff.\nif you want to see my work, hit 2, and if "
          "you want to get in touch hmu by pressing 3! otherwise, feel free to explore my site.")
    while True:
        try:
            options = int(input("[1] Go Back \n"
                                "[2] See Socials \n"
                                "[3] Contact \n"
                                "[Enter Choice]: "))
        except ValueError:
            launch()
        else:
            if options == 1:
                home()
                break
            elif options == 2:
                socials()
            elif options == 3:
                contact()
            else:
                launch()


def home():
    global location
    location = r"bin\home"
    launch()
    while True:
        try:
            options = int(input("[1] Projects \n"
                                "[2] Art \n"
                                "[3] About \n"
                                "[Enter Choice]: "))
        except ValueError:
            launch()
        else:
            if options == 1:
                projects()
                break
            elif options == 2:
                art()
                break
            elif options == 3:
                about()
                break
            else:
                launch()


# endregion
def niceProjects():
    global location
    location = r"bin\projects\important-stuff"
    launch()
    while True:
        try:
            options = int(input("[1] Go Back \n"
                                "[2] Discord Auth Bot \n"
                                "[3] random.py \n"
                                "[Enter Choice]: "))
        except ValueError:
            launch()
        else:
            if options == 1:
                projects()
                break
            elif options == 2:
                webbrowser.open("https://github.com/Scaledi/discord-auth-bot")
            elif options == 3:
                webbrowser.open("https://github.com/Scaledi/random.py")
            else:
                launch()


def socials():
    global location
    while True:
        location = r"bin\about\socials"
        launch()
        try:
            options = int(input("[1] Go Back \n"
                                "[2] Github \n"
                                "[3] Discord \n"
                                "[Enter Choice]: "))
        except ValueError:
            launch()
        else:
            if options == 1:
                about()
                break
            elif options == 2:
                webbrowser.open("https://github.com/Scaledi")
            elif options == 3:
                location = r"bin\about\contact\discord"
                launch()
                print("Ping for toast#7910")
                input("[Press enter to dismiss]:")
            else:
                launch()


def contact():
    global location
    while True:
        location = r"bin\about\contact"
        launch()
        try:
            options = int(input("[1] Go Back \n"
                                "[2] Email \n"
                                "[3] Discord \n"
                                "[Enter Choice]: "))
        except ValueError:
            launch()
        else:
            if options == 1:
                about()
                break
            elif options == 2:
                location = r"bin\about\contact\email"
                launch()
                print("ebrobot2000 at gmail.com")
                input("[Press enter to dismiss]:")
            elif options == 3:
                location = r"bin\about\contact\discord"
                launch()
                print("Ping for toast#7910")
                input("[Press enter to dismiss]:")
            else:
                launch()


# region: fancy stuff
i = random.randrange(1,5)
print(name)
while i > 0:
    print("Loading.", end="\r")
    time.sleep(0.3)
    print("Loading..", end="\r")
    time.sleep(0.3)
    print("Loading...", end="\r")
    time.sleep(0.3)
    print("           ", end="\r")
    i = i - 1
# endregion

while True:
    home()
