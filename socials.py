import discord

embed=discord.Embed(title="I found the following socials of Elise. *Dont mind the mess behind me*", description="π Instagram --> https://www.instagram.com/twitch_hatsunejuju/ \n πTwitter --> https://twitter.com/TJuju124 \n πSteam --> https://steamcommunity.com/profiles/76561198161493384/ \n π Battle.Net --> juju125#2638 \n π Youtube Channel --> https://www.youtube.com/channel/UCFK1FzoHQ3XlQaqejb3fGMg/playlists?view_as=subscriber \n  π  Youtube Vod Channel --> https://www.youtube.com/channel/UCpGrqQTMjFGFecEMd7F3YcQ?view_as=subscriber \n π Valorant ID --> SakuraElis#Pink \n π Reddit --> https://www.reddit.com/r/HatsuneJuju/ \n π PS4 IGN --> Image down below ", color=0xfe3ee4)
embed.set_image(url="https://cdn.discordapp.com/attachments/491904770236481549/866804206534524958/unknown.png")
embed.set_footer(text="π Elise her Socials π")


async def onSocialsMessage(message): 
  await message.channel.send("<:MikuStare:714726830703247362> Let me check for Elise her Socials hang on. *Papers rumbles noisies*")
  await message.channel.send(embed=embed)
  
  