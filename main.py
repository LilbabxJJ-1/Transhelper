# <----------------------------------MainImports---------------------------------------->
import discord
from discord.ext import commands
# <----------------------------------FileImports---------------------------------------->
from commandss import general as s
from commandss import mod as m
from data import IDs as d
from data import msgs as mg
from commandss import help as h
from tokens import tokens
# <-----------------------------------Bot----------------------------------------------->
# Create a bot
intents = discord.Intents.all()
activity = discord.Activity(type=discord.ActivityType.watching, name='Trans Town', url="https://discord.gg/unZUS5r5P7")
bot = commands.Bot(command_prefix=commands.when_mentioned_or('-'), case_insensitive=True, activity=activity, intents=intents, help_command=None)


@bot.event
async def on_ready():
    print(f"{bot.user.name} is online!")


@bot.event
async def on_member_join(ctx):
    chn = bot.get_channel(d.Server.welcome)
    chn2 = bot.get_channel(d.Server.logs)
    guild = bot.get_guild(d.Server.guild)
    roles = guild.get_role(985963383931166810)
    await ctx.add_roles(roles)
    await chn2.send(f"Unverified role has been given to {ctx.mention}")
    embed = discord.Embed(title=f"Welcome to Trans Town {ctx.name}",
                          description=f"﹒︵︵︵︵ ⁺. ✧ .⁺ ︵︵︵︵\n"
                                      f"""Hey {ctx.mention}!{mg.welcome}""",
                          color=0xFF10F0)
    embed.set_image(url="https://media.discordapp.net/attachments/920291832611614750/989459750662066197/ec1b529086996a4958f97c8d77feb288.gif")
    await chn.send(ctx.mention, embed=embed)


@bot.event
async def on_member_remove(ctx):
    chn = bot.get_channel(d.Server.welcome)
    await chn.send(f"{ctx.name} has left the server :(")


@bot.event
async def on_message(mes):
    if mes.content == bot.user.mention:
        await mes.channel.send("Hiya! Ya pinged? My prefix is `-`\nFor commands, do -menu")
    await bot.process_commands(mes)


@bot.command()
async def ping(ctx):
    print(d.Server.welcome)
    await ctx.send("pong!")


def run():
    bot.add_cog(s.Start(bot))
    bot.add_cog(m.Mod(bot))
    bot.add_cog(h.Help(bot))
    bot.run(tokens)


run()

