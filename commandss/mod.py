# <----------------------------------Imports---------------------------------------->
import discord
from discord.ext import commands
from data import IDs as d
from data import msgs as m
# <-----------------------------------Bot--------------------------------------------->



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
        role = ctx.guild.get_role(989628090995077190)
        has_role = False
        for i in ctx.author.roles:
            if role.id == i.id:
                has_role = True
            else:
                pass

        if has_role:
            pass
        else:
            await ctx.send("You don't have the permission to do this. Only Staff can use this")
            return

        def check(msg):
            if msg.author != self.bot.user:
                pass
            if msg.author == ctx.author:
                return True

        lol = await ctx.send("What should the title be?")
        title = await self.bot.wait_for('message', timeout=30, check=check)
        await lol.delete()
        lol2 = await ctx.send("What should the message say?")
        message = await self.bot.wait_for('message', timeout=300, check=check)
        await lol2.delete()
        lol3 = await ctx.send("Ping the channel I should send it in")
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
        try:
            await chn.channel_mentions[0].send(embed=embed)
            await when.delete()
            await ctx.send("Embed Sent!")
        except IndexError:
            await ctx.send("Couldn't find that channel!")

    @commands.command()
    async def verify(self, ctx):
        await ctx.message.delete()
        role = ctx.guild.get_role(989628090995077190)
        has_role = False
        for i in ctx.author.roles:
            if role.id == i.id:
                has_role = True
            else:
                pass
        if has_role:
            pass
        else:
            await ctx.send("You don't have the permission to do this. Only Staff can use this")
            return
        guild = self.bot.get_guild(d.Server.guild)
        chn = guild.get_channel(d.Server.gen)
        roles = guild.get_role(985963383931166810)
        roles2 = guild.get_role(985963267774120036)
        mem = ctx.message.mentions[0]
        await mem.remove_roles(roles)
        await mem.add_roles(roles2)
        embed = discord.Embed(title=f"Welcome {mem.name}", description=m.entry, color=0xFF10F0)
        await chn.send(f"<@&990140702677671936>", embed=embed)
        await ctx.send(f"{mem.name} has been verified", delete_after=5)

    @commands.command()
    async def warn(self, ctx, member, *warning):
        await ctx.message.delete()
        role = ctx.guild.get_role(989628090995077190)
        has_role = False
        for i in ctx.author.roles:
            if role.id == i.id:
                has_role = True
            else:
                pass
        if has_role:
            pass
        else:
            await ctx.send("You don't have the permission to do this. Only Staff can use this")
            return
        guild = self.bot.get_guild(d.Server.guild)
        try:
            mem = ctx.message.mentions[0]
        except IndexError:
            mem = guild.get_member(member)
        if mem is None:
            await ctx.send("That member isn't in this server")
        else:
            final = ""
            for i in warning:
                final += f"{i} "
            if len(final) < 1:
                await ctx.send("You need to give a reason")
                return
            chn = guild.get_channel(d.Server.warn)
            embed = discord.Embed(title="Warning!",
                                  description=f"{mem.mention}, you have been warned for: {final}",
                                  color=0xFF10F0)
            await chn.send(mem.mention, embed=embed)
