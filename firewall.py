import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='firewall ')

@bot.event
async def on_ready():
    print('Bot ready')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

@bot.command(pass_context=True, aliases = ['say','chickennugget'])
async def chickennuggets(ctx,arg):
    try:
        await ctx.send(arg)
    except discord.ext.commands.errors.MissingRequiredArgument:
        await ctx.send("Say something don't leave it blank")

@bot.command(pass_context=True, aliases = ['ping','pong'])
async def firewallPing(ctx):
    await ctx.send('Bounce Pong! {0} secs'.format(round(bot.latency, 1)))

@bot.command(pass_context=True, aliaese = ['about','help'])
async def firewallHelp(ctx):
    await ctx.send('Firewall help:')
    await ctx.send('Firewall Help:
        ```Usage: firewall [command] [argument]
        firewall say/chickennugget [argument]: say the desired argument. Use quotes(") for args more 
        than 2 words
        firewall ping: Test latency between bot and Discord's servers
        firewall help/about: This help Menu
        
        Contribute to firewall! https://github.com/pixdoet/firewall-bot/tree/main
        Firewall is made by Jun Ian(wok#9607)
        ```')

TOKEN = ('token :)') # insert your token here
bot.run(TOKEN)
