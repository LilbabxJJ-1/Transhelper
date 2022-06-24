# <----------------------------------Imports---------------------------------------->
import discord
from discord.ext import commands
from data import msgs as m
# <-----------------------------------Bot--------------------------------------------->


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def menu(self, ctx):
        role = ctx.guild.get_role(989628090995077190)
        has_role = False
        for i in ctx.author.roles:
            if role.id == i.id:
                has_role = True
            else:
                pass

        if has_role:
            embed = discord.Embed(title="Menu", description=m.modhelp, color=0xFF10F0)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Menu", description=m.help, color=0xFF10F0)
            await ctx.send(embed=embed)


