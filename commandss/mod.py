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
                return 1 == 1

        await ctx.message.delete()
        await ctx.channel.purge(limit=amount, check=is_pinned)
        await ctx.send(f"{amount} messages deleted and skipped all pinned messages", delete_after=5)


    @commands.command()
    async def warn(self, ctx, user: discord.member, warning):
        await ctx.send("")