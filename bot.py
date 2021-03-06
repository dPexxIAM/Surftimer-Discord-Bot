import discord
from discord.ext import commands
import json
import asyncio
import aiomysql
import os
import sys, traceback

initial_extensions = ['cogs.utils']

with open('config.json') as f:
    file_dict = json.load(f)
    token = file_dict['token']
    prefix = file_dict['prefix']
    dbhost = file_dict['dbhost']
    dbuser = file_dict['dbuser']
    dbpass = file_dict['dbpass']
    dbname = file_dict['dbname']  
    dbport = file_dict['dbport']  
	
bot = commands.Bot(command_prefix=prefix)
loop = asyncio.get_event_loop()

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()
		
print("Bot loaded successfully")
	
@bot.command()
async def mtop(ctx, map):
    conn = await aiomysql.connect(host=dbhost, port=dbport, user=dbuser, password=dbpass, db=dbname, loop=loop)
    async with conn.cursor() as cur:
        await cur.execute("SELECT name, MIN(runtimepro) FROM ck_playertimes WHERE mapname = %s AND runtimepro > -1.0 AND style = 0", (map))
        result = await cur.fetchall()
        for data in result:
            name = data[0]
            runtime = data[1]
            minutes = runtime / 60
            minutes = minutes % 60
            seconds = round(int(runtime))
            seconds = runtime % 60
            milli = round(int(runtime * 100))
            milli = milli % 100
            formatTime = "%02d:%02d:%02d" % (int(minutes), int(seconds), int(milli)) 
            await ctx.send(name + ' has the ' + map + ' record with a time of ' + str(formatTime))
    conn.close()

bot.run(token)
