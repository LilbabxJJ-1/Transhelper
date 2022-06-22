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
        await ctx.message.delete()
        for i in await ctx.channel.purge(limit=amount):
            print(i)
        await ctx.send(f"{amount} messages deleted", delete_after=5)