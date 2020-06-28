import discord
import asyncio
import requests
import sys

sys.path.append('./bots')
import cybersole
import balkobot
import phantomaio
import dasheio
import projectdestroyer
import wrathaio
import mekpreme
import adeptsupreme
import veloxpreme
import splashforcebot
import prismaio
import swftaio
import polaris
import scottbot
import tohru
from tohru import tohruL, tohruR
from scottbot import scottbotR, scottbotL
from polaris import polarisR, polarisL
from swftaio import swft, swftL
from prismaio import prism
from splashforcebot import splashforce
from veloxpreme import velox, veloxR
from adeptsupreme import adept, adeptR
from mekpreme import mek, mekR
from wrathaio import wrath, wrathR
from projectdestroyer import pdL, pdR
from dasheio import dashe, dasheR
from phantomaio import phantom, phantomR
from balkobot import balko, balkoR
from cybersole import cyber, cyberR

sys.path.append('./groups')
import threefiveone
import BounceAlerts
import Calicos
import Excluded
import GUAP
import MEKNotifyCN
import PeachyPings
import RestockWorld
import SiteSupply
import FakeMonitor
import HiddenSociety
import SabreIO
from SabreIO import sabreR, sabreL
from HiddenSociety import hiddenL, hiddenR
from FakeMonitor import fakeL, fakeR
from threefiveone import threefiveoneR
from BounceAlerts import bounceR
from Calicos import calicosR
from Excluded import excludedR
from GUAP import guapL, guapR
from MEKNotifyCN import meknL, meknR
from PeachyPings import peachyL, peachyR
from RestockWorld import rwR
from SiteSupply import ssL, ssR

token = 'YOUR TOKEN HERE'
client = discord.Client()

@client.event
async def on_ready():
    print('--------------------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--------------------')


@client.event
async def on_message(message):
	if message.content.startswith('!help'):
		embed = discord.Embed(title="Help", description="Here are all of the commands you can run!")
		embed.set_author(name="BotBroker", url="https://www.botbroker.io/", icon_url="https://pbs.twimg.com/profile_images/1202325425466134528/bQyROCKB_400x400.jpg")
		embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1202325425466134528/bQyROCKB_400x400.jpg")
		embed.add_field(name="Commands:", value="**!bots** - List of all bots\n**!groups** - List of all groups\n**!guide** - Important information before buying all bots!", inline=True)
		await message.channel.send(embed=embed)
	if message.content.startswith('!guide'):
		embed = discord.Embed(title="**BOT BUYING GUIDE**")
		embed.set_author(name="BotBroker", url="https://www.botbroker.io/", icon_url="https://pbs.twimg.com/profile_images/1202325425466134528/bQyROCKB_400x400.jpg")
		embed.add_field(name="\u200b", value="""`CYBER`\n• Bind / Unbind via https://cybersole.io/dashboard\n• Key can be reset through the bot or dashboard\n• Lifetime and Renewal (£100 / 6 months) licenses\n\n
`BALKO`\n• One time bind via Discord\n• Key can be reset through the bot and Discord\n• There are Lifetime, $40 every 6 months, and $360 / year licenses\n\n
`PHANTOM`\n• One time bind via Discord\n• Key can be reset through bot and Discord\n• Lifetime and Renewal ($60 / 6 months and $150 / 6 months) licenses\n\n""", inline=True)
		embed.add_field(name="\u200b", value="""`DASHE`\n• One time bind via https://dashe.io/sign-in\n• Full email access is recommended to secure the account\n• Discord access is transferable\n• Lifetime and Renewal ($50 / month) license\n• Renewal licenses have the Shopify and Supreme module while Lifetime only have the Shopify module\n• Lifetime users have the option to upgrade their licenses to a discounted monthly renewal rate in order to receive the Supreme module\n\n
`PROJECT DESTROYER`\n• Bind / Unbind via Discord\n• Key can be reset through the bot and Discord\n• Lifetime and Renewal ($150 / 6 months), and monthly ($35 / month) licenses\n• Lifetime licenses do not include the adidas add-on ($130 extra)\n\n
`WRATH`\n• Bind / Unbind via Discord\n• Key can be reset through the bot and Discord\n• Lifetime and Renewal licenses\n\n""", inline=False)
		embed.add_field(name="\u200b", value="""`MEKPREME`\n• Bind / Unbind via Discord\n• Key can be reset through the bot and Discord\n• Lifetime and Renewal ($60 / 6 months) licenses\n\n
`ADEPT SUPREME`\n• Bind / Unbind via https://adept-bots.com/dashboard/\n• Key can be reset through the bot, Discord, or the Dashboard\n• Optional email transfer feature which regenerates a key and delivers it to a specified email for £10\n• Cannot be rented out because you need Dashboard access to download the latest verison\n\n
`VELOX`\n• Bind / Unbind via Discord\n• Key can be reset through the bot and Discord\n• Lifetime and Renewal (Seasonal Based) licenses\n\n
`GHOST SNKRS`\n• One time bind via Discord\n• Key can be reset through the bot and Discord\n• Lifetime and Renewal ($60 / 6 months) licenses\n\n
`SPLASHFORCE`\n• UNKNOWN AT THIS TIME\n\n
`PRISM`\n• License transfer via https://prismaio.com/dashboard\n• Key can be reset through the bot and Dashboard\n Only Renewal licenses\n\n
`SWFT`\n• Discord unbindable upon request""", inline=False)
		await message.channel.send(embed=embed)
	if message.content.startswith('!bots'):
		embed = discord.Embed(title="Bots", description="List of all bots provided on BotBroker")
		embed.set_author(name="BotBroker", url="https://www.botbroker.io/bots", icon_url="https://pbs.twimg.com/profile_images/1202325425466134528/bQyROCKB_400x400.jpg")
		embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1202325425466134528/bQyROCKB_400x400.jpg")
		embed.add_field(name="Bots:", value="!cyber\n!balko\n!phantom\n!dashe\n!pd\n!wrath\n!mek\n!adept\n!velox\n!ghost\n!splashforce\n!prism\n!swft", inline=True)
		await message.channel.send(embed=embed)
	if message.content.startswith('!groups'):
		embed = discord.Embed(title="Groups", description="List of all groups provided on BotBroker")
		embed.set_author(name="BotBroker", url="https://www.botbroker.io/groups", icon_url="https://pbs.twimg.com/profile_images/1202325425466134528/bQyROCKB_400x400.jpg")
		embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1202325425466134528/bQyROCKB_400x400.jpg")
		embed.add_field(name="Groups:", value="!351\n!bounce\n!calicos\n!excluded\n!flips\n!guap\n!meknotify\n!peachy\n!rw\n!sitesupply", inline=True)
		await message.channel.send(embed=embed)
	if message.content.startswith('!cyber'):
		embed = discord.Embed(title="Cybersole", url="https://www.botbroker.io/products/cyber-aio", description="Last recorded sales for Cybersole", color=0x3fe25b)
		embed.set_thumbnail(url="https://is4-ssl.mzstatic.com/image/thumb/Purple123/v4/b3/8c/0e/b38c0e99-5e09-62c0-4de2-28e83d52ca16/AppIcon-0-0-1x_U007emarketing-0-0-0-7-0-0-sRGB-0-0-0-GLES2_U002c0-512MB-85-220-0-0.png/246x0w.png")
		embed.add_field(name="Sites:", value="**Shopify | Supreme | Footsites | Mesh**", inline=False)
		embed.add_field(name="Lifetime:", value="{}".format(cyber), inline=True)
		embed.add_field(name="Renewal:", value="{}".format(cyberR), inline=True)
		await message.channel.send(embed=embed)
	if message.content.startswith('!balko'):
		embed = discord.Embed(title="Balko", url="https://www.botbroker.io/products/balko", description="Last recorded sales for Balko", color=0x393d5b)
		embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1177062169231405056/9whojPiW_400x400.jpg")
		embed.add_field(name="Sites:", value="**Shopify | Adidas | Supreme**", inline=False)
		embed.add_field(name="Lifetime:", value="{}".format(balko), inline=True)
		embed.add_field(name="Renewal:", value="{}".format(balkoR), inline=True)
		await message.channel.send(embed=embed)
	if message.content.startswith('!phantom'):
		embed = discord.Embed(title="Phantom", url="https://www.botbroker.io/products/phantom", description="Last recorded sales for Phantom", color=0x231f21)
		embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1216808451134775296/KuKLwykd.png")
		embed.add_field(name="Sites:", value="**Footsites | Adidas | Supreme | Yeezy Supply**", inline=False)
		embed.add_field(name="Lifetime:", value="{}".format(phantom), inline=True)
		embed.add_field(name="Renewal:", value="{}".format(phantomR), inline=True)
		await message.channel.send(embed=embed)
	if message.content.startswith('!dashe'):
		embed = discord.Embed(title="Dashe", url="https://www.botbroker.io/products/dashe", description="Last recorded sales for Dashe", color=0x3d93d1)
		embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1223442739834118144/WvvIilUp_400x400.png")
		embed.add_field(name="Sites:", value="**Shopify | Supreme | Yeezy Supply**", inline=False)
		embed.add_field(name="Lifetime:", value="{}".format(dashe), inline=True)
		embed.add_field(name="Renewal:", value="{}".format(dasheR), inline=True)
		await message.channel.send(embed=embed)
	if message.content.startswith('!pd'):
		embed = discord.Embed(title="Project Destroyer", url="https://www.botbroker.io/products/project-destroyer", description="Last recorded sales for Project Destroyer", color=0xc939d5)
		embed.set_thumbnail(url="https://projectdestroyer.com/wp-content/uploads/2019/05/pfp1-1.png")
		embed.add_field(name="Sites:", value="**Shopify | Supreme | Footsites | Adidas | Yeezy Supply**", inline=False)
		embed.add_field(name="Lifetime:", value="{}".format(pdL), inline=True)
		embed.add_field(name="Renewal:", value="{}".format(pdR), inline=True)
		await message.channel.send(embed=embed)
	if message.content.startswith('!wrath'):
		embed = discord.Embed(title="Wrath", url="https://www.botbroker.io/products/wrath", description="Last recorded sales for Wrath", color=0x436bcb)
		embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1244432031263723522/XogvE7RK_400x400.jpg")
		embed.add_field(name="Sites:", value="**Shopify | Supreme | Footsites | Yeezy Supply**", inline=False)
		embed.add_field(name="Lifetime:", value="{}".format(wrath), inline=True)
		embed.add_field(name="Renewal:", value="{}".format(wrathR), inline=True)
		await message.channel.send(embed=embed)
	if message.content.startswith('!mek'):
		embed = discord.Embed(title="MEKPreme", url="https://www.botbroker.io/products/mekpreme", description="Last recorded sales for MEKPreme", color=0xdb3337)
		embed.set_thumbnail(url="https://images.squarespace-cdn.com/content/v1/5d521fe55fbb18000193bb8e/1584927320782-UQHYUW8IVYNFBVK9PD5T/ke17ZwdGBToddI8pDm48kJ-iXUMiALsiCqMow8k6utl7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QHyNOqBUUEtDDsRWrJLTmXIZ66LEW7qVrHuEzDKwcZLJQJnzBktHb7C38hLhauKf_9wJZhRvyMuxBngDLj2xm/mekpreme22.png")
		embed.add_field(name="Sites:", value="**Supreme**", inline=False)
		embed.add_field(name="Lifetime:", value="{}".format(mek), inline=True)
		embed.add_field(name="Renewal:", value="{}".format(mekR), inline=True)
		await message.channel.send(embed=embed)
	if message.content.startswith('!adept'):
		embed = discord.Embed(title="Adept Supreme", url="https://www.botbroker.io/products/adept-supreme", description="Last recorded sales for Adept Supreme", color=0xc79fea)
		embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1219904009437425665/F0Ik--2-_400x400.jpg")
		embed.add_field(name="Sites:", value="**Supreme**", inline=False)
		embed.add_field(name="Lifetime:", value="{}".format(adept), inline=True)
		embed.add_field(name="Renewal:", value="{}".format(adeptR), inline=True)
		await message.channel.send(embed=embed)
	if message.content.startswith('!velox'):
		embed = discord.Embed(title="Velox", url="https://www.botbroker.io/products/velox", description="Last recorded sales for Velox", color=0xffffff)
		embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1221980758463655937/n-NfpnHa_400x400.jpg")
		embed.add_field(name="Sites:", value="**Supreme**", inline=False)
		embed.add_field(name="Lifetime:", value="{}".format(velox), inline=True)
		embed.add_field(name="Renewal:", value="{}".format(veloxR), inline=True)
		await message.channel.send(embed=embed)
	if message.content.startswith('!ghost'):
		embed = discord.Embed(title="Ghost SNKRS", url="https://www.botbroker.io/products/ghost-snkrs", description="Last recorded sale for Ghost SNKRS", color=0xf88ba0)
		embed.set_thumbnail(url="https://theme.zdassets.com/theme_assets/2416868/3cc4cf533a299b59c945959cdf16715388fa5693.png")
		embed.add_field(name="Sites:", value="**Nike**", inline=False)
		embed.add_field(name="Lifetime:", value="{}".format(ghost), inline=True)
		embed.add_field(name="Renewal:", value="{}".format(ghostR), inline=True)
		await message.channel.send(embed=embed)
	if message.content.startswith('!splashforce'):
		embed = discord.Embed(title="Splashforce", url="https://www.botbroker.io/products/splashforce", description="Last recorded sales for Splashforce", color=0x000000)
		embed.set_thumbnail(url="https://i.imgur.com/br7M061.png")
		embed.add_field(name="Sites:", value="**Adidas | Supreme | Shopify | Yeezy Supply**", inline=False)
		embed.add_field(name="Renewal:", value="{}".format(splashforce), inline=True)
		await message.channel.send(embed=embed)
	if message.content.startswith('!prism'):
		embed = discord.Embed(title="Prism", url="https://www.botbroker.io/products/prism", description="Last recorded sales for Prism", color=0x25223E)
		embed.set_thumbnail(url="https://i.imgur.com/NxL1ajE.png")
		embed.add_field(name="Sites:", value="**Shopify | Footsites | Supreme**", inline=False)
		embed.add_field(name="Renewal:", value="{}".format(prism), inline=True)
		await message.channel.send(embed=embed)
	if message.content.startswith('!swft'):
		embed = discord.Embed(title="SwftAIO", url="https://www.botbroker.io/products/swftaio", description="Last recorded sales for SwftAIO", color=0xDC615C)
		embed.set_thumbnail(url="https://i.imgur.com/RQYnXeq.png")
		embed.add_field(name="Sites:", value="**Shopify | Mesh | Footsites**", inline=False)
		embed.add_field(name="Lifetime:", value="{}".format(swftL), inline=True)
		embed.add_field(name="Renewal:", value="{}".format(swft), inline=True)
		await message.channel.send(embed=embed)
	if message.content.startswith('!351'):
		embed = discord.Embed(title='351io', url="https://botbroker.io/groups/351io", description="Last recorded sales for 351io", color=0xffffff)
		embed.set_thumbnail(url="https://i.imgur.com/dW6eG6j.png")
		embed.add_field(name="Renewal:", value="{}".format(threefiveoneR), inline=True)
		await message.channel.send(embed=embed)
	if message.content.startswith('!bounce'):
		embed = discord.Embed(title="Bounce Alerts", url='https://www.botbroker.io/groups/bounce-alerts', description="Last recorded sales for Bounce Alerts", color=0x641EB5)
		embed.set_thumbnail(url='https://i.imgur.com/oa2bwDx.png')
		embed.add_field(name="Renewal:", value="{}".format(bounceR), inline=True)
		await message.channel.send(embed=embed)
	if message.content.startswith('!excluded'):
		embed = discord.Embed(title="Excluded", url='https://www.botbroker.io/groups/excluded', description="Last recorded sales for Excluded", color=0x987BFE)
		embed.set_thumbnail(url='https://i.imgur.com/IC75BEx.png')
		embed.add_field(name="Renewal:", value="{}".format(excludedR), inline=True)
		await message.channel.send(embed=embed)
	if message.content.startswith('!calicos'):
		embed = discord.Embed(title="Calicos", url='https://www.botbroker.io/groups/calicos', description="Last recorded sales for Calicos", color=0xFE6EC6)
		embed.set_thumbnail(url='https://i.imgur.com/LoE19nL.png')
		embed.add_field(name="Renewal:", value="{}".format(calicosR), inline=True)
		await message.channel.send(embed=embed)
	if message.content.startswith('!flips'):
		embed = discord.Embed(title="FlipsIO", url='https://www.botbroker.io/groups/flipsio', description="Last recorded sales for FlipsIO", color=0x78BDD9)
		embed.set_thumbnail(url='https://i.imgur.com/GzR5t2g.png')
		embed.add_field(name="Renewal:", value="{}".format(flipsR), inline=True)
		await message.channel.send(embed=embed)
	if message.content.startswith('!guap'):
		embed = discord.Embed(title="GUAP", url="https://www.botbroker.io/groups/guap", description='Last recorded sales for GUAP', color=0x7D29F4)
		embed.set_thumbnail(url='https://i.imgur.com/FRNUvJu.png')
		embed.add_field(name="Lifetime:", value="{}".format(guapL), inline=True)
		embed.add_field(name="Renewal:", value="{}".format(guapR), inline=True)
		await message.channel.send(embed=embed)
	if message.content.startswith('!meknotify'):
		embed = discord.Embed(title="MEKNotify CN", url="https://www.botbroker.io/groups/meknotify-cn", description='Last recorded sales for MEKNotify CN', color=0x768BAE)
		embed.set_thumbnail(url='https://i.imgur.com/MsgAs1H.png')
		embed.add_field(name="Lifetime:", value="{}".format(meknL), inline=True)
		embed.add_field(name="Renewal:", value="{}".format(meknR), inline=True)
		await message.channel.send(embed=embed)
	if message.content.startswith('!peachy'):
		embed = discord.Embed(title="Peachy Pings", url="https://www.botbroker.io/groups/peachy-pings", description='Last recorded sales for Peachy Pings', color=0xF8A47F)
		embed.set_thumbnail(url='https://i.imgur.com/mPaWntS.png')
		embed.add_field(name="Lifetime:", value="{}".format(peachyL), inline=True)
		embed.add_field(name="Renewal:", value="{}".format(peachyR), inline=True)
		await message.channel.send(embed=embed)
	if message.content.startswith('!rw'):
		embed = discord.Embed(title="Restock World", url="https://www.botbroker.io/groups/restock-world", description='Last recorded sales for Restock World', color=0x685AE3)
		embed.set_thumbnail(url='https://avatars.io/twitter/restockworld')
		embed.add_field(name="Renewal:", value="{}".format(rwR), inline=True)
		await message.channel.send(embed=embed)
	if message.content.startswith('!sitesupply'):
		embed = discord.Embed(title="Site Supply", url="https://www.botbroker.io/groups/site-supply", description='Last recorded sales for Site Supply', color=0x3F6476)
		embed.set_thumbnail(url='https://i.imgur.com/WlV0Y39.png')
		embed.add_field(name="Lifetime:", value="{}".format(ssL), inline=True)
		embed.add_field(name="Renewal:", value="{}".format(ssR), inline=True)
		await message.channel.send(embed=embed)
	if message.content.startswith('!polaris'):
		embed = discord.Embed(title="Polaris", url="https://botbroker.io/products/polaris", description='Last recorded sales for Polaris', color=0x7873E5)
		embed.set_thumbnail(url='https://res.cloudinary.com/dcbenpm7u/image/twitter_name/w_600/polarisaio.jpg')
		embed.add_field(name="Sites:", value="**Adidas | Footsites | Supreme | Shopify | YeezySupply | Mesh**", inline=False)
		embed.add_field(name="Lifetime:", value="{}".format(polarisL), inline=True)
		embed.add_field(name="Renewal:", value="{}".format(polarisR), inline=True)
		await message.channel.send(embed=embed)
	if message.content.startswith('!scottbot'):
		embed = discord.Embed(title="Scottbot", url="https://botbroker.io/products/scottbot", description='Last recorded sales for Scottbot', color=0x111111)
		embed.set_thumbnail(url='https://res.cloudinary.com/dklrin11o/image/twitter_name/w_600/scottbotv1.jpg')
		embed.add_field(name="Sites:", value="**Collectibles**", inline=False)
		embed.add_field(name="Lifetime:", value="{}".format(scottbotL), inline=True)
		embed.add_field(name="Renewal:", value="{}".format(scottbotR), inline=True)
		await message.channel.send(embed=embed)
	if message.content.startswith('!tohru'):
		embed = discord.Embed(title="TohruAIO", url="https://botbroker.io/products/tohruaio", description='Last recorded sales for TohruAIO', color=0xEE8B90)
		embed.set_thumbnail(url='https://res.cloudinary.com/dcbenpm7u/image/twitter_name/w_600/tohruaio.jpg')
		embed.add_field(name="Sites:", value="**Footsites | Supreme**", inline=False)
		embed.add_field(name="Lifetime:", value="{}".format(tohruL), inline=True)
		embed.add_field(name="Renewal:", value="{}".format(tohruR), inline=True)
		await message.channel.send(embed=embed)
	if message.content.startswith('!fake'):
		embed = discord.Embed(title="Fake Monitor", url="https://www.botbroker.io/groups/fake-monitor", description='Last recorded sales for Fake Monitor', color=0x42B4A1)
		embed.set_thumbnail(url='https://i.imgur.com/dkBeWoj.png')
		embed.add_field(name="Lifetime:", value="{}".format(fakeL), inline=True)
		embed.add_field(name="Renewal:", value="{}".format(fakeR), inline=True)
		await message.channel.send(embed=embed)
	if message.content.startswith('!hidden'):
		embed = discord.Embed(title="Hidden Society", url="https://www.botbroker.io/groups/hidden-society", description='Last recorded sales for Hidden Society', color=0x6AE59B)
		embed.set_thumbnail(url='https://res.cloudinary.com/dcbenpm7u/image/twitter_name/w_600/ahiddensociety.jpg')
		embed.add_field(name="Lifetime:", value="{}".format(hiddenL), inline=True)
		embed.add_field(name="Renewal:", value="{}".format(hiddenR), inline=True)
		await message.channel.send(embed=embed)
	if message.content.startswith('!sabre'):
		embed = discord.Embed(title="SabreIO", url="https://www.botbroker.io/groups/sabreio", description='Last recorded sales for SabreIO', color=0x20203C)
		embed.set_thumbnail(url='https://res.cloudinary.com/dklrin11o/image/twitter_name/w_600/sabreio.jpg')
		embed.add_field(name="Lifetime:", value="{}".format(sabreL), inline=True)
		embed.add_field(name="Renewal:", value="{}".format(sabreR), inline=True)
		await message.channel.send(embed=embed)
client.run(token)
