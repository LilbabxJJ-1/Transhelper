# <----------------------------------MainImports---------------------------------------->
import discord
from discord.ext import commands
# <----------------------------------FileImports---------------------------------------->
from commandss import start as s
from commandss import mod as m
# <-----------------------------------Bot----------------------------------------------->
# Create a bot
bot = commands.Bot(command_prefix=commands.when_mentioned_or('-'), case_insensitive=True)




@bot.event
async def on_ready():
    print(f"{bot.user.name} is online!")


@bot.command()
async def taco(ctx):
    await ctx.message.mentions[0].edit(nick="Taco")
    await ctx.send(f"{ctx.message.mentions[0].name}'s name has been changed to taco lol")


@bot.command()
async def nickname(ctx, nick):
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


@bot.command()
async def clear(ctx, amount=5):
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"{amount} messages deleted", delete_after=5)



def run():
    bot.add_cog(s.Start(bot))
    bot.add_cog(m.Mod(bot))
    bot.run("")
run()