# warning, the animated pfp won't show in the developer portal but it will show in servers and dms! and anywhere!

import discord
import aiohttp

client = discord.Client(intents=discord.Intents.default())
TOKEN = ''

new_profile_pic_url = 'https://i.ibb.co' 
# use this host upload an image go to the link copy as image address and paste it here


@client.event
async def on_ready():
    print('Bot is ready.')

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(new_profile_pic_url) as resp:
                image_data = await resp.read()
        
        await client.user.edit(avatar=image_data)
        print('Profile picture changed successfully.')
    except Exception as e:
        print('Failed to change profile picture:', e)

client.run(TOKEN)

