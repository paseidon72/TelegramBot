import json

import discord
from discord.ext import commands
import config, sqlite3
import string, json

bot = commands.Bot(command_prefix='!', intents=discord.Intents())

@bot.event
async def on_ready():
    print('Bot ready to communicate')

    global base, cur
    base = sqlite3.connect('poryadok.db')
    cur = base.cursor()
    if base:
        print('Database connected...OK!')

@bot.event
async def on_member_join(member):
    await member.send('Привет я бот слежу за порядком, посмотреть команды с !инфо')
    for ch in bot.get_guild(member.guild.id).channels:
        if ch.name == 'основной':
            await bot.get_channel(ch.id).send(f'{member}, круто что ты с нами в лс !инфо')

@bot.event
async def on_member_remove(member):
    for ch in bot.get_guild(member.guild.id).channels:
        if ch.name == 'основной':
            await bot.get_channel(ch.id).send(f'{member}, нам будет тебя нехватать')

@bot.command()
async def test(ctx):
    await ctx.send('Тест пройдено')

@bot.command()
async def инфо(ctx, arg=None):
    author = ctx.message.author
    if arg == None:
        await ctx.send(f'{author.mention} Введите:\n!инфо общая\n!инфо команды')
    elif arg == 'общая':
        await ctx.send(f'{author.mention} Я слежу за порядком в чате. 3 предупреждения за мат - БАН')
    elif arg == 'команды':
        await ctx.send(f'{author.mention} !test - Бот онлайн?\n !статус - мои предупреждения')
    else:
        await ctx.send(f'{author.mention} Такой команды нет...')

@bot.command()
async def статус(ctx):
    base.execute('CREATE TABLE IF NOT EXISTS {}(userid INT, count INT)'.format(ctx.message.guild.name))
    base.commit()
    warnings = cur.execute('SELECT * FROM {} WHERE userid == ?'.format(ctx.message.guild.name)\
                           ,(ctx.message.author.id,)).fetchone()
    if warnings == None:
        await ctx.send(f'{ctx.message.author.mention}, предупреждений нет!!')
    else:
        await ctx.send(f'{ctx.message.author.mention}, у вас {warnings[1]} предупреждений??')

@bot.event
async def on_message(message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.content.split(' ')}\
            .intersection(set(json.load(open('combined.json')))) != set():
        await message.channel.send(f'{message.author.mention}, ууу..??')
        await message.delete()

        name = message.guild.name

        base.execute('CREATE TABLE IF NOT EXISTS {}(userid INT, count INT)'.format(name))
        base.commit()

        warnings = cur.execute('SELECT * FROM {} WHERE userid == ?'.format(name), (message.author.id,)).fetchone()
        if warnings == None:
            cur.execute('INSERT INTO {} VALUES(?, ?)'.format(name),(message.author.id,1))
            await message.channel.send(f'{message.author.mention}, первое предупреждение')

        elif warnings[1] == 1:
            cur.execute('UPDATE {} SET count == ? WHERE userid == ?'.format(name),(2,message.author.id))
            base.commit()
            await message.channel.send(f'{message.author.mention}, 2 предупреждение')

        elif warnings[2] == 2:
            cur.execute('UPDATE {} SET count == ? WHERE userid == ?'.format(name), (3, message.author.id))
            base.commit()
            await message.channel.send(f'{message.author.mention}, забанен')
            await message.author.ban(reason='Нецензурные выражения')
    await bot.process_commands(message)

bot.run(config.TOKEN)






















