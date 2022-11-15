import discord
from discord.ext import commands

token = 'PUT_TOKEN_HERE'
intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = 'https://ogu.gg/al1'))
    print(f'{bot.user} has logged in successfully.')
    try:
        await bot.tree.sync()
        print(f'{bot.user} has synced commands successfully.')
    except Exception as e:
        print(e)

@bot.tree.command(name = 'badge', description = 'Get your active developer badge!')
async def badge(interaction: discord.Interaction):
    embed = discord.Embed(title = 'Success!', description = 'The command was run successfully, check back at https://discord.com/developers/active-developer in 24 hours to claim your badge.')
    embed.set_author(name = 'al1', url = 'https://ogu.gg/al1', icon_url = 'https://cdn.discordapp.com/attachments/1038211803164979241/1041921759814885436/yes.png')
    await interaction.response.send_message(embed = embed)

bot.run(token)