# <----------------------------------Imports---------------------------------------->
import discord
from discord.ext import commands
import random
import time
from data import IDs as d
# <-----------------------------------Bot--------------------------------------------->



class Start(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def divide(self, ctx, a: int, b: int):
        await ctx.send(f"If you put {a} into {b} groups, you get {a / b} in each group.")


    @commands.command()
    async def pronouns(self, ctx, name, pronoun):
        ll = ""
        ll2 = []
        for i in pronoun:
            if i == "/":
                ll2.append(ll)
                ll = ""
            else:
                ll += i
        ll2.append(ll)
        t_choices1 = [f"{name} is a cool person, {ll2[0]} is a great friend of mine, I love {ll2[1].lower()}!",
                      f"Have you heard from {name}? We're going to the mall with {ll2[1].lower()} today! Let me know when "
                      f"{ll2[0].lower()} pops up!",
                      f"{name} is too cool for school 😎. {ll2[0]} is so amazing. One reason I enjoy being around "
                      f"{ll2[1].lower()} is because we have great conversations.",
                      ]

        await ctx.send("Processing...", delete_after=2)
        time.sleep(3)
        await ctx.send(random.choice(t_choices1))


    @commands.command(aliases=["nick"])
    async def nickname(self, ctx, nick):
            l = ["<", "@", "#", ">"]
            if PermissionError:
                await ctx.send("Cannot change Owners nickname")
            for i in l:
                if i in nick:
                    await ctx.send("Nickname cannot contain these symbols: **<, @, #, >**")
                    return
            if nick == "":
                await ctx.send("Nickname is empty")
            elif len(nick) > 32:
                await ctx.send("Nickname is too long")
            elif len(nick) < 2:
                await ctx.send("Nickname is too short")
            else:
                await ctx.message.author.edit(nick=nick)
                await ctx.send(f"{ctx.message.author.name}'s nickname has been changed to {nick}")

    @nickname.error
    async def nickname_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please Provide a nickname")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send("I don't have the perms to do this")
        else:
            print(error)

    @commands.command()
    async def loaf(self, ctx):
        embed = discord.Embed(title="Love Loaf")
        loafs = ["https://redstaryeast.com/wp-content/uploads/2014/09/Cinnamon-Heart-Bread.jpg",
                 "https://images-gmi-pmc.edge-generalmills.com/94108f4d-6772-4d07-86d8-822f293be659.jpg"]
        embed.set_image(url=random.choice(loafs))
        await ctx.send(embed=embed)

    @commands.command()
    async def avatar(self, ctx, id=None):
        if id is None:
            mem = self.bot.get_user(ctx.author.id)
            embed = discord.Embed(title=f"{ctx.author.name}'s Avatar", color=0xFF10F0)
            print(mem.avatar)
            embed.set_image(url=f"https://cdn.discordapp.com/avatars/{mem.id}/{mem.avatar}.png")
            await ctx.send(embed=embed)
        else:
            mem = self.bot.get_user(int(id))
            if mem is None:
                await ctx.send("Couldn't Find that user")
                return
            embed = discord.Embed(title=f"{mem.name}'s Avatar", color=0xFF10F0)
            embed.set_image(url=f"https://cdn.discordapp.com/avatars/{mem.id}/{mem.avatar}.png")
            await ctx.send(embed=embed)
