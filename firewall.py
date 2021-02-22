import discord
from discord.ext import commands
import lyrical
import animefy
# import searchify # we wait until searchify is fixed
import random

bot = commands.Bot(command_prefix='fw ')

@bot.event
async def on_ready():
    print('Bot ready')
    await bot.change_presence(activity=discord.Game("I hate you! >_< "))
@bot.event
async def on_message(message):
    if message.author == bot.user:
        print("Loop")
    if message.content.startswith("firewall"):
        await message.send("The prefix for firewall has changed to fw")
    await bot.process_commands(message)

# fw say
@bot.command(pass_context=True, aliases = ['say','chickennugget'])
async def chickennuggets(ctx,arg):
    if arg == "":
        await ctx.send("Say something don't leave it blank")
    elif arg == " ":
        await ctx.send("No spaces please")
    else:
        await ctx.send(arg)

#fw ping
@bot.command(pass_context=True, aliases = ['ping','pong'])
async def firewallPing(ctx):
    await ctx.send('Bounce Pong! {0} secs'.format(bot.latency, 1))

#fw contribute
@bot.command(pass_context=True, aliases = ['contribute'])
async def firewallContributeMessage(ctx):
    await ctx.send('Github: https://github.com/pixdoet/firewall-bot/')

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
    await ctx.send("You mwaed :kissing_heart: " + whoToMwa + "!")
#fw respects
@bot.command(pass_context=True, aliases = ['f','respects','respect'])
async def firewallRespect(ctx, whoToF):
    await ctx.send("You paid respects[f] to " + whoToF)
    await ctx.send("https://cdn1.dotesports.com/wp-content/uploads/2018/09/08153731/Untitled.png")
    await message.add_reaction(":regional_indicator_f:")

#fw givebrain
@bot.command(pass_context=True, aliases = ['givebrain'])
async def firewallGiveBrain(ctx, whoToGive):
    await ctx.send("You gave your brain :brain: to " + whoToGive)

#fw cry
@bot.command(pass_context=True, aliases = ['cry'])
async def firewallCry(ctx):
    await ctx.send("Boo Hoo Hoo:sob:")
    await ctx.send("https://fsa.zobj.net/crop.php?r=DxAJwethh781KLDbcjIvfG4FEdv3XKovrPPEb7emfvYIe6nikzZfBCeY5re7NFthuz1WUS-S9cLz2hQKCGr6qPoF3QiPJmSsjFSzcD0YfecG0u0dvAoL6o1iekCAOlaJ3nRVS-Hvy3l9BPLs")

#fw sob
@bot.command(pass_context=True, aliases = ['sob'])
async def firewallSob(ctx):
    await ctx.send("Boo Hoo Hoo:sob:")
    await ctx.send("https://i.pinimg.com/originals/2d/78/28/2d78285f218a3692496922c7635c5daf.gif")

#fw racist
@bot.command(pass_context=True, aliases = ['racist'])
async def firewallRacist(ctx):
    await ctx.send("Racism is not cool. No race is better than another, no race is worse than another.")
    await ctx.send("Learn more: https://en.wikipedia.org/wiki/Anti-racism")

#fw pingmeme
@bot.command(pass_context=True, aliases = ['pingmeme'])
async def firewallPingmeme(ctx):
    await ctx.send("Other bots: Ping normally")
    await ctx.send("Firewall: \n **HGDBKHHDCLAMKNVKEFNSNLCJNSLNWDJNCKS**")

#fw google (wait)
#@bot.command(pass_context=True, aliases = ['google','search','gsearch'])
#async def firewallSearch(ctx,searchQuery, searchResultsNum):
    #gsearchres = searchify.searchg(searchQuery, searchResultsNum)
    #await ctx.send("Results: \n" + gsearches)
    
#fw version
@bot.command(pass_context=True, aliases = ['version','ver'])
async def firewallVersion(ctx):
    await ctx.send("Firewall Helios 1.6bf1")

#fw changelog
@bot.command(pass_context=True, aliases = ['changelog'])
async def firewallChangelog(ctx):
    await ctx.send("Full changelog here: https://github.com/pixdoet/firewall-bot/blob/main/firewall-changelog")
    await ctx.send("Firewall Helios 1.6bf1 \n -Removed commands: \n     -search/google/gesearch\n     \n-Changed say command for empty/null message handling")

TOKEN = ('') # insert your token here
bot.run(TOKEN)
