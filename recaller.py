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
    if message.author == client.user:
        return

    # test run bots messaging capability in admin channel.
    if message.content.startswith("$test") and message.channel.name == 'cadet-admin':
        channel = client.get_channel(1011069501229518949)
        await channel.send('Hello World. Ready to Recall.')
        await channel.send('Ready to recall all squadrons.')

    # "$squadron1" recalls squadron 1
    if message.content.startswith("$squadron1") and message.channel.name == 'cadet-admin':
        channel = client.get_channel(900427739180458056)
        await channel.send('@everyone RECALL RECALL RECALL, LIKE THIS MESSAGE ASAP TO REPORT ACCOUNTABILITY! CHECK ON YOUR WINGMEN!')

    # "$squadron3" recalls squadron 2
    if message.content.startswith("$squadron2") and message.channel.name == 'cadet-admin':
        channel = client.get_channel(900429872214716456)
        await channel.send('@everyone RECALL RECALL RECALL, LIKE THIS MESSAGE ASAP TO REPORT ACCOUNTABILITY! CHECK ON YOUR WINGMEN!')

    # "$squadron3" recalls squadron 3
    if message.content.startswith("$squadron3") and message.channel.name == 'cadet-admin':
        channel = client.get_channel(900430073071546368)
        await channel.send('@everyone RECALL RECALL RECALL, LIKE THIS MESSAGE ASAP TO REPORT ACCOUNTABILITY! CHECK ON YOUR WINGMEN!')

# -----

# confirm bot is running
@client.event
async def on_ready():
    print("RUNNING")

# run, get token
if __name__ == '__main__':
    client.run(TOKEN)


