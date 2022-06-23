# <----------------------------------Imports---------------------------------------->
import discord
from discord.ext import commands
# <-----------------------------------Bot--------------------------------------------->
bot = commands.Bot(command_prefix=commands.when_mentioned_or('-'), case_insensitive=True)



class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clear(self, ctx, amount=10):
        def is_pinned(msg):
            if not msg.pinned:
                return True

        await ctx.message.delete()
        await ctx.channel.purge(limit=amount, check=is_pinned)
        await ctx.send(f"{amount} messages deleted and skipped all pinned messages", delete_after=5)


    @commands.command(hidden=True)
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
        final = ""
        for i in message.content:
            if i == "\n":
                final += "\n"
            else:
                final += i
        embed = discord.Embed(title=title.content, description=final, color=0xFF10F0)
        if message.attachments:
            embed.set_image(url=message.attachments[0].url)
        await chn.channel_mentions[0].send(embed=embed)
        await when.delete()
        await ctx.send("Embed Sent!")