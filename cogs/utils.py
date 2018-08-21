import time
import aiohttp
import discord
import asyncio
from discord.ext import commands

class UtilsCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.send("SBC Bot is working correctly.")

    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(title="SBC Bot", color=0xc24700)
        embed.add_field(name="Author", value="Evan#1880")
        embed.add_field(name="Invite", value="https://discordapp.com/oauth2/authorize?&client_id=426171940663853057&scope=bot")
        await ctx.send(embed=embed)
    
    @commands.command()
    async def members(self, ctx):
        guild = ctx.guild
        embed=discord.Embed(title="Member Count", description=guild.member_count, color=0xc24700)
        await ctx.send(embed=embed)
		
def setup(bot):
    bot.add_cog(UtilsCog(bot))