# <----------------------------------Imports---------------------------------------->
import discord
from discord.ext import commands
import random
import time
# <-----------------------------------Bot--------------------------------------------->
bot = commands.Bot(command_prefix=commands.when_mentioned_or('-'), case_insensitive=True)


class Start(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def divide(self, ctx, a: int, b: int):
        await ctx.send(ctx.channel.id)
        await ctx.send(f"If you put {a} into {b} groups, you get {a / b} in each group.")


    @commands.command()
    async def test(self, ctx, name, pronouns):
        ll = ""
        ll2 = []
        for i in pronouns:
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


    @commands.command()
    async def embed(self, ctx):
        def check(msg):
            if msg.author != self.bot.user:
                return True

        lol = await ctx.send("What should the title be?")
        title = await self.bot.wait_for('message', timeout=30, check=check)
        await lol.delete()
        lol2 = await ctx.send("What should the message say?")
        message = await self.bot.wait_for('message', timeout=300, check=check)
        await lol2.delete()
        lol3 = await ctx.send("Ping the channel I show send it in")
        chn = await self.bot.wait_for("message", timeout=30, check=check)
        await lol3.delete()
        when = await ctx.send("Processing...")
        time.sleep(1.5)
        await when.delete()
        await ctx.send("Embed Sent!")
        final = ""
        for i in message.content:
            if i == "\n":
                final += "\n"
            else:
                final += i
        embed = discord.Embed(title=title.content, description=final, color=0xFF10F0)
        await chn.channel_mentions[0].send(embed=embed)

