# recall bot build 0.15 beta
# for use with OU DET 675 (EXP)

# you will need this installed to edit/ the .py
# DISCORD TOKEN is unique to every server. Keep private at all costs!
import discord
DISCORD_TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXX"

# use env to hide token, token can be found through dev mode
# GET RID OF THIS AND JUST HARD CODE IN THE TOKEN!!!! 31Aug
TOKEN = DISCORD_TOKEN
# -----

# turns the bot on
client = discord.Client()


# preset messages -----
@client.event
async def on_message(message):
    # it has to have this to work
    if message.author == client.user:
        return

    # "$recall" in the channel "recall" triggers the bot
    if message.content.startswith("$recall") and message.channel.name == 'cadet-admin':
        # this tells it where to look, channel ID fills in the Xs:
        channel = client.get_channel(XXXXXXXXXXXXXXXXXXXXXXX)
        # this is the message that it sends:
        await channel.send('@everyone THIS IS A TEST RECALL! GO THIS LINK ASAP: https://forms.gle/csDrvKMXdtBJhYv17')

    # test run bots messaging capability in admin channel.
    if message.content.startswith("$test") and message.channel.name == 'cadet-admin':
        channel = client.get_channel(XXXXXXXXXXXXXXXXXXXXXXX)
        await channel.send('Hello World. Ready to Recall.')
# -----

# confirm bot is running
@client.event
async def on_ready():
    print("RUNNING")

# run, get token
if __name__ == '__main__':
    client.run(TOKEN)


