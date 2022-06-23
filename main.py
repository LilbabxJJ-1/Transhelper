# <----------------------------------MainImports---------------------------------------->
import discord
from discord.ext import commands
# <----------------------------------FileImports---------------------------------------->
from commandss import start as s
from commandss import mod as m
from data import IDs as d
from data import msgs as mg
# <-----------------------------------Bot----------------------------------------------->
# Create a bot
intents = discord.Intents.all()
activity = discord.Activity(type=discord.ActivityType.watching, name='Trans Town', url="https://discord.gg/unZUS5r5P7")
bot = commands.Bot(command_prefix=commands.when_mentioned_or('-'), case_insensitive=True, activity=activity, intents=intents)



@bot.event
async def on_ready():
    print(f"{bot.user.name} is online!")



@bot.event
async def on_member_join(ctx):
    chn = bot.get_channel(d.Server.welcome)
    await chn.send(f"""Hey {ctx.mention}!{mg.welcome}""")

@bot.command()
async def ping(ctx):
    print(d.Server.welcome)
    await ctx.send("pong!")

def run():
    bot.add_cog(s.Start(bot))
    bot.add_cog(m.Mod(bot))
    bot.run("")
run()