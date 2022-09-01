# PythonDiscordBot
Made for use with AFROTC Detachment 675's Discord Messaging Server.

$test: a test message to see if the bot is online and functioning
$recall: sends out recall message to entire server


Needs: Discord Dev Account (to retrieve auth token for DISCORD_TOKEN)
       Channel ID's where commands will be sent, and where the bot will send messages.
       Python 3
      
### METHODS FOR INSTALLING PYTHON (for editing/use):
1. https://www.python.org/downloads/ (ALL OPERATING SYSTEMS)
2. WINDOWS STORE
  - check in terminal: **where python**
3. MAC TERMINAL
  - using homebrew: **$ brew install python 3**
  - verify: **$ -a python, $ which python**
4. IDE (for editing)
  - I used Pycharm by Jetbrains (free) 
  - Will let you write/run python right away!


# All cadet admins/users will need python in order to turn the bot on/off.
### Why?
The bot needs something to run off of. By hitting "run" in your IDE or running the .py, your computer becomes the host for the bot. By default bot will run as long as your computer is awake, but if your IDE sleeps, it might turn off.

This is OK. If a recall is scheduled, its very easy to just run the program to *"power on"* the Recall Bot. If it is an emergency recall, the bot can be turned on in ***under 10 seconds*** at any time.

### Is there a way to keep it on 24/7?
Not for free. It can be web hosted (where a server runs the code 24/7), but that costs money and can become expensive

### Is there another way to recall?
Yes. The link for the recall form can be sent to commanders and be sent manaully to all cadets. If there is a want, a webpage can be built to do this automatically via email.
