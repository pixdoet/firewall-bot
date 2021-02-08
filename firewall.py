import discord
from discord.ext import commands
import lyrical
import animefy
import random

bot = commands.Bot(command_prefix='fw ')

@bot.event
async def on_ready():
    print('Bot ready')
    await bot.change_presence(activity=discord.Game("It's fw instead of Firewall"))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

# fw say
@bot.command(pass_context=True, aliases = ['say','chickennugget'])
async def chickennuggets(ctx,arg):
    try:
        await ctx.send(arg)
    except discord.ext.commands.errors.MissingRequiredArgument:
        await ctx.send("Say something don't leave it blank")

#fw ping
@bot.command(pass_context=True, aliases = ['ping','pong'])
async def firewallPing(ctx):
    await ctx.send('Bounce Pong! {0} secs'.format(bot.latency, 1))

#fw contribute
@bot.command(pass_context=True, aliases = ['contribute'])
async def firewallContributeMessage(ctx):
    await ctx.send('Github: https://github.com/pixdoet/firewall-bot/blob/main/firewall.py')

#fw lyrics
@bot.command(pass_context=True, aliases = ['lyrics'])
async def firewallGetLyrics(ctx,sname,aname):
    lyrics = lyrical.find(sname,aname)
    await ctx.send(lyrics)

#fw kekw
@bot.command(pass_context=True, aliases = ['kekw'])
async def firewallKekw(ctx):
    await ctx.send('https://www.streamscheme.com/wp-content/uploads/2020/07/kekw-emote.jpg')

#fw WOK
@bot.command(pass_context=True, aliases = ['wok'])
async def firewallWok(ctx):
    await ctx.send("THE KING OF THE WOKS HAS ARRIVED")
    await ctx.send('https://my-test-11.slatic.net/p/3074a0dace3a3e245e25fb4275a3c867.jpg')
    await ctx.send(":WOK::WOK::WOK::WOK::WOK::WOK:")

#fw thomas
@bot.command(pass_context=True, aliases = ['thomas'])
async def firewallThomas(ctx):
    await ctx.send("Why you call Thomas he's gae")

#fw version
@bot.command(pass_context=True, aliases = ['version','ver'])
async def firewallVersion(ctx):
    await ctx.send("Firewall Helios 1.4bf1")

#fw anime
@bot.command(pass_context=True, aliases = ['anime'])
async def firewallAnime(ctx,animeTitle):
    synopsis = animefy.search(animeTitle)
    await ctx.send(synopsis)

#fw nooneasked
@bot.command(pass_context=True, aliases = ['nooneasked'])
async def firewallNooneasked(ctx):
    await ctx.send("https://qph.fs.quoracdn.net/main-qimg-468b02bba8c4b3086c3dc7245709a3d6")

#fw randomsauce
@bot.command(pass_context=True, aliases = ['randomsauce'])
async def firewallRandomsauce(ctx):
    rndsauce = random.randrange(0,340999)
    await ctx.send(rndsauce)

#fw mwa
@bot.command(pass_context=True, aliases = ['mwa','mua'])
async def firewallMwa(ctx,whoToMwa):
    await ctx.send("You mwaed :kissing_heart:" + whoToMwa + "!")
#fw respects
@bot.command(pass_context=True, aliases = ['f','respects','respect'])
async def firewallRespect(ctx, whoToF):
    await ctx.send("You paid respects[f] to " + whoToF)
    await ctx.send("https://cdn1.dotesports.com/wp-content/uploads/2018/09/08153731/Untitled.png")
    
#fw changelog
@bot.command(pass_context=True, aliases = ['changelog'])
async def firewallChangelog(ctx):
    await ctx.send("Firewall Helios 1.4bf2 \n -Added commands: \n     -f/respects\n     \n-")

TOKEN = ('') # insert your token here
bot.run(TOKEN)
